import random
from enum import Enum

random.seed()


class Modes(Enum):
    MINOR = 0
    MAJOR = 1


#===================================================================#
#             Mappings for Emotions to Spotify Params               #
#===================================================================#


class SpotifyItem:
    def __init__(self, emotion_type,
                 emojis,
                 mode,
                 danceability=None,
                 energy=None,
                 explicit=False,
                 tempo=None,
                 valence=None,
                 loudness=None):

        self.mode = mode
        self.emotion_type = emotion_type
        assert isinstance(emojis, (list, tuple, str))
        self.emojis = \
            [emojis] if isinstance(emojis, str) else emojis
        self.danceability = danceability
        self.energy = energy
        self.explicit = explicit
        self.tempo = tempo
        self.valence = valence
        self.loudness = loudness

    def __str__(self):
        return f"{self.emotion_type}: {self.emojis[0]}"

    def get_target_dict(self):
        r = {}
        r['target_mode'] = r['min_mode'] = r['max_mode'] = self.mode.value

        for key, value in (
            ('target_danceability', 0.5 + self.danceability/2.0 if self.danceability else None),
            ('target_energy', 0.5 + self.energy/2.0 if self.energy else None),
            ('target_tempo', 150 + self.tempo*150 if self.tempo else None),
            ('target_valence', 0.5 + self.valence/2.0 if self.valence else None),
            ('target_loudness', -10 + self.loudness * 10 if self.loudness else None)
        ):
            if value is not None:
                r[key] = float(value)
        return r


class Emotions:
    PURITY = SpotifyItem("Purity", "(＊´ㅂ`＊)", valence=+0.4, energy=-0.4, loudness=-0.5, mode=Modes.MAJOR)
    SIMPLICITY = SpotifyItem("Simplicity", "▽・x・▽", valence=+0.4, energy=-0.4, loudness=-0.5, mode=Modes.MAJOR)
    NAIVITY = SpotifyItem("Naivity", " ҉٩(´︶`)۶҉", tempo=-0.3, energy=+0.0, mode=Modes.MAJOR)
    INNOCENTLY_SAD = SpotifyItem("Innocently Sad", "", valence=-0.3, energy=-0.3, loudness=-0.5, mode=Modes.MINOR)
    LOVE_SICK = SpotifyItem("Love-Sick", "", valence=-0.3, energy=+0.2, mode=Modes.MINOR)
    DESPAIR = SpotifyItem("Despair", "", valence=-0.3, energy=+0.5, loudness=+0.5, mode=Modes.MINOR)
    WAILING = SpotifyItem("Wailing", "。・゜・(ノД`)・゜・。﻿", tempo=-0.1, valence=-0.4, energy=+0.6, loudness=+0.5, mode=Modes.MINOR)
    WEEPING = SpotifyItem("Weeping", "（ つ Д ｀）", tempo=-0.1, valence=-0.4, energy=+0.5, loudness=-0.3, mode=Modes.MINOR)
    GRIEF = SpotifyItem("Grief", "(இɷஇ )", tempo=-0.3, valence=-0.6, energy=+0.5, loudness=-0.3, mode=Modes.MINOR)
    DEPRESSIVE = SpotifyItem("Depressive", "", tempo=-0.5, valence=-0.6, mode=Modes.MINOR)
    TRIUMPHANT = SpotifyItem("Triumphant", "٩(๑❛ᴗ❛๑)۶", danceability=+0.6, valence=+0.4, energy=+0.5, loudness=+0.7, mode=Modes.MAJOR)
    WAR_CRIES = SpotifyItem("War Cries", "ε٩ (๑•̀ω•́๑)۶з", danceability=+0.6, tempo=+0.4, valence=+0.4, loudness=+0.7, mode=Modes.MAJOR)
    SERIOUS = SpotifyItem("Serious", "(,,ō_ō )", danceability=-0.4, valence=-0.3, energy=+0.5, loudness=+0.5, mode=Modes.MINOR)
    BROODING_WORRIES = SpotifyItem("Brooding Worries", "", danceability=-0.4, valence=-0.3, energy=-0.5, loudness=+0.5, mode=Modes.MINOR)
    DEEP_DISTRESS = SpotifyItem("Deep Distress", "◝(๑⁺᷄д⁺᷅๑)◞՞", valence=-0.7, energy=+0.5, loudness=+0.7, mode=Modes.MINOR)
    EXISTENTIAL_ANGST = SpotifyItem("Existential Angst", "", valence=-0.5, tempo=-0.2, energy=+0.5, loudness=+0.7, mode=Modes.MINOR)
    ANXIETY = SpotifyItem("Anxiety", "(・・；)", tempo=+0.3, valence=-0.3, energy=+0.6, loudness=+0.4, mode=Modes.MINOR)
    DEVOTION = SpotifyItem("Devotion", "Orz", valence=+0.4, energy=-0.7, loudness=-0.7, mode=Modes.MAJOR)
    HONEST_COMMUNION = SpotifyItem("Honest Communication", "", valence=+0.4, energy=-0.7, loudness=-0.7, mode=Modes.MAJOR)
    QUARRELSOME = SpotifyItem("Quarrelsome", "(੭ु´͈ ᐜ `͈)੭ु⁾⁾", tempo=+0.3, valence=+0.3, danceability=+0.3, energy=+0.6, loudness=+0.4, mode=Modes.MAJOR)
    READY_TO_FIGHT = SpotifyItem("Ready to Fight", "(੭•̀ω•́)੭̸*✩⁺˚﻿", tempo=+0.3, valence=+0.3, danceability=+0.3, energy=+0.9, loudness=+0.4, mode=Modes.MAJOR)
    #GRIEF = SpotifyItem("")
    RESTFULNESS = SpotifyItem("Restfulness", "(✿˘︶˘*)", danceability=-0.4, valence=+0.3, energy=-0.9, loudness=-1.0, mode=Modes.MAJOR)
    FURIOUS = SpotifyItem("Furious", "(๑•̀д•́๑)و ̑̑", tempo=+0.4, valence=0.0, loudness=+0.5, energy=+0.5, mode=Modes.MAJOR)
    QUICK_TEMPERED = SpotifyItem("Quick-Tempered", "₍₍ ᕕ(бωб)ᕗ⁾⁾", tempo=+0.4, valence=0.0, loudness=+0.5, energy=+0.5, mode=Modes.MAJOR)
    ANGRY_BUT_COMPOSED = SpotifyItem("Angry but Composed", "\\(´-∀-`)/", tempo=+0.0, valence=-0.5, energy=-0.5, mode=Modes.MAJOR) # ???
    DEEPEST_DEPRESSION = SpotifyItem("Deepest Depression", "", tempo=-0.6, valence=-0.7, loudness=-0.5, energy=+0.9, mode=Modes.MINOR)
    LAMENT_OVER_LOSS = SpotifyItem("Lament Over Loss", "", tempo=-0.4, valence=-0.3, loudness=-0.5, energy=+0.5, mode=Modes.MINOR)
    TRIUMPH_OVER_EVIL = SpotifyItem("Triumph Over Evil", "", tempo=+0.1, valence=+0.4, loudness=+0.5, energy=+0.8, mode=Modes.MAJOR)
    SIGHS_OF_RELIEF = SpotifyItem("Sighs of Relief", "(￣ー￣)", tempo=+0.1, valence=+0.4, loudness=-0.2, energy=+0.0, mode=Modes.MAJOR)
    GLOOMY = SpotifyItem("Gloomy", "(´ェ｀)", tempo=-0.5, valence=-0.4, energy=-0.6, loudness=-0.5, mode=Modes.MINOR)
    PASSIONATE_RESENTMENT = SpotifyItem("Passionate Resentment", "( • ̀ω•́ )✧", valence=-0.4, energy=+0.8, mode=Modes.MINOR)
    MAGNIFICENT = SpotifyItem("Magnificent", "", tempo=+0.2, valence=+0.4, loudness=+0.5, energy=+0.5, mode=Modes.MAJOR)
    FANTASY = SpotifyItem("Fantasy", "( •̀ .̫ •́ )✧", tempo=+0.2, valence=+0.4, loudness=-0.5, energy=+0.5, mode=Modes.MAJOR)
    DISCONTENT = SpotifyItem("Discontent", "(◦`~´◦)", tempo=+0.3, valence=-0.4, loudness=+0.0, energy=-0.3, mode=Modes.MINOR)
    UNEASINESS = SpotifyItem("Uneasiness", "Σ(゜д゜;)", tempo=+0.3, valence=-0.4, loudness=+0.0, energy=+0.2, mode=Modes.MINOR)
    ETERNITY = SpotifyItem("Eternity", "", tempo=+0.1, valence=+0.4, loudness=+0.5, energy=+0.6, mode=Modes.MAJOR)
    JUDGEMENT = SpotifyItem("Judgement", "", tempo=+0.1, valence=+0.4, loudness=+0.5, energy=+0.6, mode=Modes.MAJOR)
    LAMENTATIONS = SpotifyItem("Lamentations", "", tempo=-0.3, valence=-0.4, energy=+0.2, loudness=+0.2, mode=Modes.MINOR)
    MOANING = SpotifyItem("Moaning", "", tempo=-0.3, valence=-0.4, energy=+0.2, loudness=+0.2, mode=Modes.MINOR)
    JOYFUL = SpotifyItem("Joyful", "♪( ´θ｀)ノ", tempo=+0.2, valence=+0.4, energy=+0.4, loudness=-0.2, mode=Modes.MAJOR)
    OPTIMISTIC = SpotifyItem("Optimistic", "", tempo=+0.2, valence=+0.4, energy=+0.4, loudness=-0.2, mode=Modes.MAJOR)
    #JOYFUL = SpotifyItem("")
    HOPEFUL_ASPIRATIONS = SpotifyItem("Hopeful Aspirations", "ψ(｀∇´)ψ", tempo=+0.2, energy=+0.9, loudness=+0.2, mode=Modes.MAJOR)
    TERRIBLE = SpotifyItem("Terrible", "", danceability=-0.5, valence=-0.4, loudness=+0.6, mode=Modes.MINOR)
    BLASPHEMOUS = SpotifyItem("Blasphemous", "", danceability=-0.5, valence=-0.4, loudness=+0.6, mode=Modes.MINOR)
    UNCONTROLLED_PASSIONS = SpotifyItem("Uncontrolled Passions", "‘`,、(๑´∀｀๑) ‘`,、’`,、", tempo=+0.8, danceability=+0.5, loudness=+0.8, mode=Modes.MAJOR)
    WILD = SpotifyItem("Wild", "ʅ(◜◡⁰)ʃ", tempo=+1.0, danceability=+0.5, loudness=+0.8, mode=Modes.MAJOR)
    SOLITARY = SpotifyItem("Solitary", "", tempo=-0.3, valence=+0.3, energy=-0.7, loudness=-0.3, mode=Modes.MINOR)
    PATIENCE = SpotifyItem("Patience", "(￣▽￣)", tempo=-0.3, valence=+0.3, energy=-0.7, loudness=-0.3, mode=Modes.MINOR)
    TENDER = SpotifyItem("Tender", "", valence=+0.4, energy=-0.7, loudness=-0.3, mode=Modes.MAJOR)
    GRACEFUL = SpotifyItem("Graceful", "", valence=+0.4, energy=-0.7, loudness=-0.3, mode=Modes.MAJOR)

    @staticmethod
    def get_random_key():
        return random.choice([i for i in Emotions.__iter__()])

    @staticmethod
    def __iter__():
        r = []
        for i in dir(Emotions):
            attr = getattr(Emotions, i)
            if isinstance(attr, SpotifyItem):
                r.append(attr)
        return r
