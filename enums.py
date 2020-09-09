import random
from enum import Enum

random.seed()


#===================================================================#
#             Mappings for Emotions to Spotify Params               #
#===================================================================#


class SpotifyItem:
    def __init__(self, emotion_type,
                 emojis,
                 danceability=None,
                 energy=None,
                 explicit=False,
                 tempo=None,
                 valence=None):

        self.emotion_type = emotion_type
        assert isinstance(emojis, (list, tuple, str))
        self.emojis = \
            [emojis] if isinstance(emojis, str) else emojis
        self.danceability = danceability
        self.energy = energy
        self.explicit = explicit
        self.tempo = tempo
        self.valence = valence

    def __str__(self):
        return f"{self.emotion_type}: {self.emojis[0]}"

    def get_target_dict(self):
        r = {}
        for key, value in (
            ('target_danceability', self.danceability),
            ('target_energy', self.energy),
            #('target_explicit', self.explicit),
            ('target_tempo', self.tempo),
            ('target_valence', self.valence)
        ):
            if value is not None:
                r[key] = float(value)
        return r


class Emotions:
    PURITY = SpotifyItem("Purity", "(＊´ㅂ`＊)", valence=+0.4)
    SIMPLICITY = SpotifyItem("Simplicity", "▽・x・▽", valence=+0.4)
    NAIVITY = SpotifyItem("Naivity", " ҉٩(´︶`)۶҉", tempo=-0.3)
    INNOCENTLY_SAD = SpotifyItem("Innocently Sad", "", valence=-0.3)
    LOVE_SICK = SpotifyItem("Love-Sick", "", valence=-0.3)
    DESPAIR = SpotifyItem("Despair", "", valence=-0.3)
    WAILING = SpotifyItem("Wailing", "。・゜・(ノД`)・゜・。﻿", tempo=-0.1, valence=-0.4)
    WEEPING = SpotifyItem("Weeping", "（ つ Д ｀）", tempo=-0.1, valence=-0.4)
    GRIEF = SpotifyItem("Grief", "(இɷஇ )", tempo=-0.3, valence=-0.6)
    DEPRESSIVE = SpotifyItem("Depressive", "", tempo=-0.5, valence=-0.6)
    TRIUMPHANT = SpotifyItem("Triumphant", "٩(๑❛ᴗ❛๑)۶", danceability=+0.2, valence=+0.4)
    WAR_CRIES = SpotifyItem("War Cries", "ε٩ (๑•̀ω•́๑)۶з", danceability=+0.6, tempo=+0.4, valence=+0.4)
    SERIOUS = SpotifyItem("Serious", "(,,ō_ō )", danceability=-0.4, valence=-0.3)
    BROODING_WORRIES = SpotifyItem("Brooding Worries", "", danceability=-0.4, valence=-0.3)
    DEEP_DISTRESS = SpotifyItem("Deep Distress", "◝(๑⁺᷄д⁺᷅๑)◞՞")
    EXISTENTIAL_ANGST = SpotifyItem("Existential Angst", "", valence=-0.5, tempo=-0.2)
    ANXIETY = SpotifyItem("Anxiety", "(・・；)", tempo=+0.3, valence=-0.3)
    DEVOTION = SpotifyItem("Devotion", "Orz", valence=+0.4)
    HONEST_COMMUNION = SpotifyItem("Honest Communication", "", valence=+0.4)
    QUARRELSOME = SpotifyItem("Quarrelsome", "(੭ु´͈ ᐜ `͈)੭ु⁾⁾", tempo=+0.3, valence=+0.3, danceability=+0.3)
    READY_TO_FIGHT = SpotifyItem("Ready to Fight", "(੭•̀ω•́)੭̸*✩⁺˚﻿", tempo=+0.3, valence=+0.3, danceability=+0.3)
    #GRIEF = SpotifyItem("")
    RESTFULNESS = SpotifyItem("Restfulness", "(✿˘︶˘*)", danceability=-0.4, valence=+0.3)
    FURIOUS = SpotifyItem("Furious", "(๑•̀д•́๑)و ̑̑", tempo=+0.4)
    QUICK_TEMPERED = SpotifyItem("Quick-Tempered", "₍₍ ᕕ(бωб)ᕗ⁾⁾", tempo=+0.4)
    ANGRY_BUT_COMPOSED = SpotifyItem("Angry but Composed", "\\(´-∀-`)/", tempo=+0.4)
    DEEPEST_DEPRESSION = SpotifyItem("Deepest Depression", "", tempo=-0.6, valence=-0.7)
    LAMENT_OVER_LOSS = SpotifyItem("Lament Over Loss", "", tempo=-0.4, valence=-0.3)
    TRIUMPH_OVER_EVIL = SpotifyItem("Triumph Over Evil", "", tempo=+0.1, valence=+0.4)
    SIGHS_OF_RELIEF = SpotifyItem("Sighs of Relief", "(￣ー￣)", tempo=+0.1, valence=+0.4)
    GLOOMY = SpotifyItem("Gloomy", "(´ェ｀)", valence=-0.4)
    PASSIONATE_RESENTMENT = SpotifyItem("Passionate Resentment", "( • ̀ω•́ )✧", valence=-0.4)
    MAGNIFICENT = SpotifyItem("Magnificent", "", tempo=+0.2, valence=+0.4)
    FANTASY = SpotifyItem("Fantasy", "( •̀ .̫ •́ )✧", tempo=+0.2, valence=+0.4)
    DISCONTENT = SpotifyItem("Discontent", "(◦`~´◦)", tempo=+0.3, valence=-0.4)
    UNEASINESS = SpotifyItem("Uneasiness", "Σ(゜д゜;)", tempo=+0.3, valence=-0.4)
    ETERNITY = SpotifyItem("Eternity", "", tempo=+0.1, valence=+0.4)
    JUDGEMENT = SpotifyItem("Judgement", "", tempo=+0.1, valence=+0.4)
    LAMENTATIONS = SpotifyItem("Lamentations", "", tempo=-0.3, valence=-0.4)
    MOANING = SpotifyItem("Moaning", "", tempo=-0.3, valence=-0.4)
    JOYFUL = SpotifyItem("Joyful", "♪( ´θ｀)ノ", tempo=+0.2, valence=+0.4)
    OPTIMISTIC = SpotifyItem("Optimistic", "", tempo=+0.2, valence=+0.4)
    #JOYFUL = SpotifyItem("")
    HOPEFUL_ASPIRATIONS = SpotifyItem("Hopeful Aspirations", "ψ(｀∇´)ψ")
    TERRIBLE = SpotifyItem("Terrible", "", danceability=-0.5, valence=-0.4)
    BLASPHEMOUS = SpotifyItem("Blasphemous", "", danceability=-0.5, valence=-0.4)
    UNCONTROLLED_PASSIONS = SpotifyItem("Uncontrolled Passions", "‘`,、(๑´∀｀๑) ‘`,、’`,、", tempo=+0.4, danceability=+0.5)
    WILD = SpotifyItem("Wild", "ʅ(◜◡⁰)ʃ", tempo=+0.4, danceability=+0.5)
    SOLITARY = SpotifyItem("Solitary", "", tempo=-0.3, valence=+0.3)
    PATIENCE = SpotifyItem("Patience", "(￣▽￣)", tempo=-0.3, valence=+0.3)
    TENDER = SpotifyItem("Tender", "", valence=+0.4)
    GRACEFUL = SpotifyItem("Graceful", "", valence=+0.4)


#===================================================================#
#                        Musical Key Mappings                       #
#===================================================================#


class _KeyType:
    def __init__(self, name, pitch_class, minor_major, attrs):
        self.name = name
        self.pitch_class = pitch_class
        self.minor_major = minor_major
        self.attrs = attrs

    def __str__(self):
        return f'{self.name} ' \
               f'{self.pitch_class} ' \
               f'{self.minor_major} ' \
               f'{" ".join(str(i) for i in self.attrs)}'

    def get_target_dict(self):
        r = {}
        for i in self.attrs:
            r.update(i.get_target_dict())
        return r


class Modes(Enum):
    MINOR = 0
    MAJOR = 1


class MusicalKeys:
    # The great explanations of different musical keys from
    # https://ledgernote.com/blog/interesting/musical-key-characteristics-emotions/
    # The mappings to pitch key numbers
    # https://en.wikipedia.org/wiki/Pitch_class
    # See also in Spotify API docs:
    # ..[[TODO]]

    C_MAJOR = _KeyType("C Major", 0, Modes.MAJOR, [
        Emotions.PURITY, Emotions.SIMPLICITY, Emotions.NAIVITY
    ])
    C_MINOR = _KeyType("C Minor", 0, Modes.MINOR, [
        Emotions.INNOCENTLY_SAD, Emotions.LOVE_SICK
    ])
    CSHARP_MINOR = _KeyType("C♯ Minor", 1, Modes.MINOR, [
        Emotions.DESPAIR, Emotions.WAILING, Emotions.WEEPING
    ])
    DFLAT_MAJOR = _KeyType("D♭ Major", 1, Modes.MAJOR, [
        Emotions.GRIEF, Emotions.DEPRESSIVE
    ])
    D_MAJOR = _KeyType("D Major", 2, Modes.MAJOR, [
        Emotions.TRIUMPHANT, Emotions.WAR_CRIES
    ])
    D_MINOR = _KeyType("D Minor", 2, Modes.MINOR, [
        Emotions.SERIOUS, Emotions.BROODING_WORRIES
    ])
    DSHARP_MINOR = _KeyType("D♯ Minor", 3, Modes.MINOR, [
        Emotions.DEEP_DISTRESS, Emotions.EXISTENTIAL_ANGST, Emotions.ANXIETY
    ])
    EFLAT_MAJOR = _KeyType("E♭ Major", 3, Modes.MAJOR, [
        Emotions.DEVOTION, Emotions.HONEST_COMMUNION
    ])
    E_MAJOR = _KeyType("E Major", 4, Modes.MAJOR, [
        Emotions.QUARRELSOME, Emotions.READY_TO_FIGHT
    ])
    E_MINOR = _KeyType("E Minor", 4, Modes.MINOR, [
        Emotions.RESTFULNESS, #Emotions.GRIEF
    ])
    F_MAJOR = _KeyType("F Major", 5, Modes.MAJOR, [
        Emotions.FURIOUS, Emotions.QUICK_TEMPERED, Emotions.ANGRY_BUT_COMPOSED
    ])
    F_MINOR = _KeyType("F Minor", 5, Modes.MINOR, [
        Emotions.DEEPEST_DEPRESSION, Emotions.LAMENT_OVER_LOSS
    ])
    FSHARP_MAJOR = _KeyType("F♯ Major", 6, Modes.MAJOR, [
        Emotions.TRIUMPH_OVER_EVIL, Emotions.SIGHS_OF_RELIEF
    ])
    FSHARP_MINOR = _KeyType("F♯ Minor", 6, Modes.MINOR, [
        Emotions.GLOOMY, Emotions.PASSIONATE_RESENTMENT
    ])
    G_MAJOR = _KeyType("G Major", 7, Modes.MAJOR, [
        Emotions.MAGNIFICENT, Emotions.FANTASY
    ])
    G_MINOR = _KeyType("G Minor", 7, Modes.MINOR, [
        Emotions.DISCONTENT, Emotions.UNEASINESS
    ])
    AFLAT_MAJOR = _KeyType("A♭ Major", 8, Modes.MAJOR, [
        Emotions.ETERNITY, Emotions.JUDGEMENT
    ])
    AFLAT_MINOR = _KeyType("A♭ Major", 8, Modes.MINOR, [
        Emotions.LAMENTATIONS, Emotions.MOANING
    ])
    A_MAJOR = _KeyType("A Major", 9, Modes.MAJOR, [
        Emotions.JOYFUL, Emotions.OPTIMISTIC
    ])
    A_MINOR = _KeyType("A Minor", 9, Modes.MINOR, [
        Emotions.TENDER, Emotions.GRACEFUL
    ])
    BFLAT_MAJOR = _KeyType("B♭ Major", 10, Modes.MAJOR, [
        Emotions.JOYFUL, Emotions.HOPEFUL_ASPIRATIONS
    ])
    BFLAT_MINOR = _KeyType("B♭ Minor", 10, Modes.MINOR, [
        Emotions.TERRIBLE, Emotions.BLASPHEMOUS
    ])
    BMAJOR = _KeyType("B Major", 11, Modes.MAJOR, [
        Emotions.UNCONTROLLED_PASSIONS, Emotions.WILD
    ])
    BMINOR = _KeyType("B Minor", 11, Modes.MINOR, [
        Emotions.SOLITARY, Emotions.PATIENCE
    ])

    @staticmethod
    def get_random_key():
        return random.choice([i for i in MusicalKeys.__iter__()])

    @staticmethod
    def __iter__():
        r = []
        for i in dir(MusicalKeys):
            attr = getattr(MusicalKeys, i)
            if isinstance(attr, _KeyType):
                r.append(attr)
        return r


