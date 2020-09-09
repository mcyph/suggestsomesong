import os
import csv
import random
import cherrypy
import requests
from pprint import pprint
from os.path import exists
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader

from enums import MusicalKeys

env = Environment(loader=FileSystemLoader('./templates'))
load_dotenv(os.path.expanduser('~/.env'))


COUNTRY_CODES = [
    ["au", 'Australia'],
    ["jp", 'Japan'],
    ["gb", 'UK'],
    ["us", 'US'],
    ["hk", "Hong Kong"],
    ["tw", "Taiwan"],
    ["es", "Spain"],
    ["fr", "France"],
    ["kr", "South Korea"],
    ["my", "Malaysia"],
]


class WebApp:
    def __init__(self):
        pass

    @cherrypy.expose
    def index(self, country="au"):
        # First, we'll get the CSV
        assert country in [i[0] for i in COUNTRY_CODES]

        CHARTS_PATH = f'charts/{country}.csv'
        if not exists(CHARTS_PATH):
            with open(CHARTS_PATH, 'w', encoding='utf-8') as f:
                f.write(requests.get(f'https://spotifycharts.com/regional/{country}/daily/latest/download').text)

        with open(CHARTS_PATH, 'r', encoding='utf-8') as f:
            ids = [i[-1].split('/')[-1] for i in csv.reader(f)][2:]
            random.shuffle(ids)
            ids = ','.join(ids[:5])

        musical_key = MusicalKeys.get_random_key()
        print(str(musical_key))

        CLIENT_ID = os.environ.get('CLIENT_ID') or "YOUR KEY HERE"
        CLIENT_SECRET = os.environ.get('CLIENT_SECRET') or "YOUR_KEY_HERE"

        grant_type = 'client_credentials'
        body_params = {'grant_type': grant_type}

        url = 'https://accounts.spotify.com/api/token'
        token_raw = requests.post(url, data=body_params, auth=(CLIENT_ID, CLIENT_SECRET)).json()
        token = token_raw["access_token"]
        auth_header = {'Authorization': "Bearer {}".format(token)}

        params = {
            # 'seed_genres': random.choice(genres['genres']),
            'seed_tracks': ids,
            'min_key': musical_key.pitch_class,
            'min_mode': musical_key.minor_major.value,
            'max_key': musical_key.pitch_class,
            'max_mode': musical_key.minor_major.value,
            'target_key': musical_key.pitch_class,
            'target_mode': musical_key.minor_major.value,
            'min_popularity': 50,
            'market': 'AU'
        }
        params.update(musical_key.get_target_dict())
        # print(params)
        recommendations = requests.get(
            'https://api.spotify.com/v1/recommendations',
            params=params,
            headers=auth_header
        ).json()
        # pprint(recommendations)

        tracks = sorted(
            recommendations['tracks'],
            key=lambda i: i['popularity'],
            reverse=True
        )

        #print()
        for track in tracks:
            track['artist'] = "/".join(i["name"] for i in track['artists'])
            #print(
            #    f'* {"/".join(i["name"] for i in track["artists"])} - {track["name"]}: {track["external_urls"]["spotify"]} (popularity {track["popularity"]})')

        return env.get_template('index.html').render(
            tracks=tracks,
            musical_key=musical_key,
            sel_country=country,
            country_codes=COUNTRY_CODES
        )


if __name__ == '__main__':
    cherrypy.quickstart(WebApp(), '/', config={
        'global': {
            'server.socket_host': '0.0.0.0',
            'server.socket_port': 3007,
            #'environment': 'production',
        },
        '/': {

        }
    })