#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description="""
Attempts a very rough translation of a D'ni sentence.

Examples:

dnitransl.py ".lehnah biv kehnehn tehnehsh ehrthbantee meh keelehntee""
" journey all is simply a series from  steps"

dnitransl.py -n ".lena biv kenen teneš erþbæntí me kílentí"
" journey all is simply a series from  steps"
""", formatter_class=RawTextHelpFormatter)

parser.add_argument("-n", "--nts",   action='store_true', help="New Transliteration Standard")
parser.add_argument("-d", "--debug", action='store_true', help="prints the parsed words")
parser.add_argument('phrase', action="store", type=str, help="a D'ni phrase")
args = parser.parse_args()



def ots2nts(in_ots):
    out_nts = in_ots.replace("ch", "ç")
    out_nts = out_nts.replace("Ch", "Ç")
    out_nts = out_nts.replace("CH", "Ç")
    out_nts = out_nts.replace("ts", "c")
    out_nts = out_nts.replace("Ts", "C")
    out_nts = out_nts.replace("TS", "C")
    out_nts = out_nts.replace("kh", "x")
    out_nts = out_nts.replace("Kh", "X")
    out_nts = out_nts.replace("KH", "X")
    out_nts = out_nts.replace("dh", "ð")
    out_nts = out_nts.replace("Dh", "Ð")
    out_nts = out_nts.replace("DH", "Ð")
    out_nts = out_nts.replace("sh", "š")
    out_nts = out_nts.replace("Sh", "Š")
    out_nts = out_nts.replace("SH", "Š")
    out_nts = out_nts.replace("th", "þ")
    out_nts = out_nts.replace("Th", "Þ")
    out_nts = out_nts.replace("TH", "Þ")
    out_nts = out_nts.replace("ih", "i")
    out_nts = out_nts.replace("Ih", "I")
    out_nts = out_nts.replace("IH", "I")
    out_nts = out_nts.replace("í", "á")
    out_nts = out_nts.replace("Í", "Á")
    out_nts = out_nts.replace("ay", "é")
    out_nts = out_nts.replace("Ay", "É")
    out_nts = out_nts.replace("AY", "É")
    out_nts = out_nts.replace("ee", "í")
    out_nts = out_nts.replace("Ee", "Í")
    out_nts = out_nts.replace("EE", "Í")
    out_nts = out_nts.replace("oy", "ó")
    out_nts = out_nts.replace("Oy", "Ó")
    out_nts = out_nts.replace("OY", "Ó")
    out_nts = out_nts.replace("oo", "ú")
    out_nts = out_nts.replace("Oo", "Ú")
    out_nts = out_nts.replace("OO", "Ú")
    out_nts = out_nts.replace("å", "æ")
    out_nts = out_nts.replace("Å", "Æ")
    out_nts = out_nts.replace("a", "æ")
    out_nts = out_nts.replace("A", "Æ")
    out_nts = out_nts.replace("æh", "ah")
    out_nts = out_nts.replace("Æh", "AH")
    out_nts = out_nts.replace("ÆH", "AH")
    out_nts = out_nts.replace("ah", "a")
    out_nts = out_nts.replace("Ah", "A")
    out_nts = out_nts.replace("AH", "A")
    out_nts = out_nts.replace("eh", "e")
    out_nts = out_nts.replace("Eh", "E")
    out_nts = out_nts.replace("EH", "E")
    out_nts = out_nts.replace("uh", "u")
    out_nts = out_nts.replace("Uh", "U")
    out_nts = out_nts.replace("UH", "U")
    out_nts = out_nts.replace("æi", "é")
    out_nts = out_nts.replace("Æi", "É")
    out_nts = out_nts.replace("ÆI", "É")
    return out_nts

def translate(dniword):
    dnidict = {
        "abcí": "basalt",
        "abcíec": "basaltic",
        "acú": "ready",
        "ago": "well",
        "alga": "(?)",
        "alon": "crown(?)",
        "ano": "water",
        "anoec": "wet",
        "anotam": "lava",
        "aní": "become",
        "ar": "go(?)",
        "aro": "other",
        "arotan": "outsider",
        "arta": "do(?)",
        "aríu": "protect",
        "aríutan": "protector",
        "aríutav": "protection",
        "aró": "attend(?)",
        "atmé": "stop(?)",
        "ave": "error",
        "avo": "Father(?)",
        "azmorelu": "Osmorella(?)",
        "aça": "light(?)",
        "b'ken": "to be",
        "ba": "beast",
        "ba'ro": "bahro",
        "bacana": "map",
        "bacen": "map",
        "bacentan": "cartographer",
        "bantano": "island",
        "bar": "(?)",
        "barel": "make",
        "bareltan": "God",
        "bareltav": "made",
        "baro": "bahro",
        "baronet": "phosphorescent",
        "barta": "accomplish(?)",
        "bavanin": "hidden(?)",
        "baš": "sense(?)",
        "bel": "claim",
        "ben": "for",
        "bexe": "compel",
        "bigto": "blessing",
        "biran": "sea(?)",
        "biv": "all",
        "bivdil": "everything",
        "bivrov": "everyone",
        "bišta": "tunnel",
        "blo": "about",
        "boken": "I will be",
        "bokenem": "you will be",
        "bokenen": "s/he will be",
        "bokenet": "we will be",
        "bokentí": "you will be",
        "bokenít": "they will be",
        "bonú": "acid",
        "bonúec": "acidic",
        "borta": "purpose(?)",
        "bot": "(?)",
        "brí": "two",
        "bríec": "second",
        "brún": "tube",
        "bugšo": "(?)",
        "bæntí": "series",
        "bæš": "sense(?)",
        "béx": "link",
        "bíra": "keep",
        "bírí": "maintain",
        "bírítan": "maintainer",
        "búgin": "creature",
        "can": "always",
        "cano": "everlasting",
        "canoš": "permanently",
        "canril": "never",
        "carú": "full(?)",
        "cav": "live",
        "cavan": "immortal",
        "chil": "main",
        "co": "of",
        "cofa": "horn",
        "cogal": "sunny",
        "coid": "glow",
        "coidal": "glowing",
        "con": "foundation",
        "cosatav": "possession(?)",
        "cotó": "child",
        "cotótí": "children",
        "cédor": "(?)",
        "címa": "need",
        "címaal": "needed",
        "cúnú": "greet",
        "cúté": "guinea pig",
        "d'ní": "D'ni",
        "da'ko": "marble",
        "daban": "alembic(?)",
        "dag": "(?)",
        "dako": "marble",
        "datam": "firemarble",
        "daš": "dome towers",
        "delin": "mist",
        "desíké": "puzzle",
        "devokæn": "hope",
        "don": "like",
        "doren": "(?)",
        "dormað": "defeat",
        "dova": "world",
        "dratol": "(?)",
        "du": "food",
        "déjí": "path",
        "dóha": "machine",
        "dú": "food",
        "dú'šol": "cater",
        "dú'šoltan": "caterer",
        "eder": "rest",
        "een": "any",
        "eg": "(?)",
        "el": "high",
        "elaþ": "elite(?)",
        "elaþ": "highest ones(?)",
        "elemar": "spore",
        "elon": "raise(?)",
        "elonet": "uplifting(?)",
        "elían": "upper class(?)",
        "elíaniþ": "upper class(?)",
        "emelan": "(?)",
        "emí": "decide(?); win(?)",
        "endé": "build",
        "endétan": "builder",
        "entan": "honesty(?)",
        "enyaloþ": "sickly",
        "enyælo": "sick",
        "erem": "skill",
        "etaf": "(?)",
        "fa": "one",
        "faec": "first",
        "fala": "fold",
        "fam": "far",
        "fasí": "twenty-five",
        "fasíec": "twenty-fifth",
        "faðo": "experience",
        "faš": "near",
        "fel": "row",
        "feltan": "rower",
        "fena": "story",
        "fentasenta": "historian",
        "ferem": "dry",
        "filað": "top",
        "fité": "look(?)",
        "flin": "order",
        "foles": "watch(?)",
        "foršu": "(?)",
        "fuš": "change color(?)",
        "fúru": "sufficient",
        "fúsa": "call",
        "fúsatav": "name",
        "galon": "ground",
        "galpo": "cave",
        "gan": "empire",
        "garano": "ocean",
        "garkal": "storm",
        "garkalec": "stormy",
        "garo": "great",
        "garoþ": "greatness",
        "garoš": "greatly",
        "gartavo": "6 hours",
        "garten": "Garten",
        "garísen": "garrison",
        "gaþ": "yet",
        "ge'dan": "wisdom",
        "gedí": "surprise(?)",
        "gel": "write",
        "geltan": "writer",
        "geltav": "writings",
        "gera": "center(?)",
        "geran": "foundation(?)",
        "gerano": "foundation(?)",
        "gestó": "Art",
        "ghen": "Gehn",
        "gica": "safe",
        "gicaþ": "safety",
        "gid": "excavate",
        "gidtav": "excavation",
        "gilo": "plant",
        "gimit": "immediate",
        "gira": "steam(?)",
        "glas": "drink",
        "glo": "begin",
        "go": "(?)",
        "gola": "justice(?)",
        "golantan": "judge",
        "gonaþ": "poor(?)",
        "gopa": "because",
        "gor": "time",
        "goran": "30 seconds",
        "gorayæn": "clock",
        "gormet": "now",
        "gormot": "then",
        "gorven": "soon",
        "graner": "circle(?)",
        "gulem": "strait(?)",
        "gæta": "due",
        "góré": "straight",
        "h'rot": "(?)",
        "hapo": "combine",
        "har": "year",
        "harten": "wait(?)",
        "haza": "white",
        "her": "number",
        "hern": "room",
        "hev": "word",
        "hevkor": "lexicon",
        "hevo": "swarm",
        "híbor": "fifteen",
        "híborec": "fifteenth",
        "hígabrí": "seventeen",
        "hígabríec": "seventeenth",
        "hígafa": "sixteen",
        "hígafaec": "sixteenth",
        "hígasen": "eighteen",
        "hígasenec": "eighteenth",
        "hígator": "nineteen",
        "hígatorec": "nineteenth",
        "hík": "rifle",
        "húcéþ": "benevolence(?)",
        "húr": "find",
        "húsaté": "satisfied(?)",
        "iglarno": "temporary",
        "ilæis": "power",
        "inæltav": "opportunity(?)",
        "iné": "more than",
        "irvæn": "mineral",
        "isyír": "revere",
        "ixa": "(?)",
        "iðsé": "line",
        "jaga": "warrant(?)",
        "jakúþ": "Devil",
        "jerú": "possible",
        "jerúþ": "possibility",
        "jima": "prophecy",
        "jixa": "remain(?)",
        "k'cí": "happy",
        "k'teš": "entertain",
        "kag": "original",
        "kageš": "originally",
        "kanhag": "(?)",
        "kanræd": "think",
        "kantin": "oppress(?)",
        "kantinaloþ": "oppressed(?)",
        "kantintan": "oppressor(?)",
        "kazí": "detour",
        "kelaní": "antelope",
        "ken": "I am",
        "kenem": "you are",
        "kenen": "is",
        "kenet": "we are",
        "kentí": "you are",
        "kenít": "are",
        "kera": "brave",
        "keraþ": "Brave One",
        "keso": "change",
        "kesotan": "changer",
        "kesotav": "change",
        "kevo": "another",
        "kevoþ": "another",
        "keštav": "warning",
        "kino": "surrender(?)",
        "kiri": "krill fly(?)",
        "kirin": "desert sand",
        "klé": "example",
        "klé": "example",
        "koca": "gate",
        "koken": "I was",
        "kokenem": "were",
        "kokenen": "was",
        "kokenet": "were",
        "kokentí": "were",
        "kokenít": "were",
        "kor": "book",
        "kor'nía": "Blank Book",
        "kor'vax": "Linking Book",
        "korfa": "First Book",
        "korman": "Descriptive Book",
        "korvax": "Linking Book",
        "kota": "locked door",
        "kro": "move",
        "kædiš": "Kadish",
        "kæligo": "council",
        "kæm": "what",
        "kæmdol": "why",
        "kæmfa": "which",
        "kæmrov": "who",
        "kæmto": "where",
        "kæt": "only",
        "kíba": "obey",
        "kíla": "endure(?)",
        "kílen": "step",
        "kúan": "stream",
        "kúza": "depart(?)",
        "l'": "has ",
        "lan": "only",
        "lasa": "seal",
        "laþ": "elite(?)",
        "laþ": "highest ones(?)",
        "lem": "ink",
        "lena": "journey",
        "lenita": "idiot",
        "lesa": "sealed",
        "leš": "rule",
        "lis": "arrive",
        "lon": "discover",
        "lonep": "discovery(?)",
        "lorag": "grace(?)",
        "loræg": "grace(?)",
        "læn": "gain(?)",
        "lésú": "carry",
        "lésútan": "carrier",
        "líam": "part(?)",
        "líaniþ": "division(?)",
        "líša": "whole(?)",
        "líšan": "whole",
        "lómat": "though",
        "lúk": "survey",
        "lúpa": "precaution(?)",
        "m'la": "lizard",
        "magen": "powers(?)",
        "mala": "come",
        "man": "existence",
        "manšú": "die",
        "manšútav": "death",
        "manšútavting": "mortality(?)",
        "manšúþ": "death-bringer",
        "marent": "follow",
        "marg": "layer",
        "marn": "create",
        "marntan": "creator",
        "marntav": "creation",
        "maryéša": "fan(?)",
        "matan": "leave(?)",
        "maðo": "succeed(?)",
        "megóré": "straight out",
        "melin": "outer",
        "mepord": "(?)",
        "mer": "watch",
        "merk": "poisoned water",
        "mes": "require",
        "met": "this",
        "meúr": "you're welcome",
        "mileš": "overwhelm(?)",
        "min": "woman",
        "miro": "toxic",
        "mišo": "universe",
        "mišta": "construct",
        "mištatav": "construction",
        "mo": "that(?)",
        "mor": "mother(?)",
        "mor'ox'mor": "grandmother",
        "mor'ox'por": "grandmother(?)",
        "moroxmor": "grandmother",
        "moroxpor": "grandmother(?)",
        "morpa": "queen",
        "mot": "which",
        "motí": "those",
        "muxon": "complex",
        "máru": "desire(?)",
        "máúd": "means(?)",
        "mægen": "powers(?)",
        "mælo": "forget",
        "mæðo": "succeed(?)",
        "mís": "speak",
        "místan": "speaker",
        "místav": "speech",
        "mít": "there",
        "múden": "fortune",
        "múší": "invention(?)",
        "n'": "around",
        "nadan": "mushroom",
        "nadanec": "mushroomy",
        "naga": "learn(?)",
        "nagé": "learn(?)",
        "nava": "master",
        "naš": "part",
        "ne": "around",
        "nefex": "(?)",
        "nekis": "bend",
        "nekisal": "bent",
        "nekisaloþ": "bent",
        "nem": "gather(?)",
        "nesít": "(?)",
        "nesít": "(?)",
        "neze": "read",
        "nogin": "ignore(?)",
        "noref": "final",
        "nudatav": "disaster(?)",
        "næ'grenis": "brittle",
        "né": "root",
        "négabrí": "twelve",
        "négafa": "eleven",
        "négasen": "thirteen",
        "négator": "fourteen",
        "névú": "ten",
        "névúec": "tenth",
        "ní": "new",
        "nía": "new",
        "nícavé": "suffer",
        "nígeš": "merely",
        "oenazo": "hope",
        "ogel": "age(?)",
        "oglan": "ancient",
        "oko": "black",
        "olíx": "(?)",
        "omd": "(?)",
        "omšíno": "(?)",
        "oner": "just",
        "ox": "of",
        "ošan": "lose",
        "ošanin": "lost",
        "pabó": "bless",
        "pac": "city",
        "pal": "anyway(?)",
        "pam": "or",
        "pan": "trust",
        "para": "great",
        "parano": "sea(?)",
        "paraþ": "greatness",
        "partavo": "hour",
        "parx": "pray(?)",
        "peké": "equal(?)",
        "pelúl": "(?)",
        "peraþ": "(?)",
        "pilel": "receive",
        "pirin": "rubbed(?)",
        "pišo": "belong",
        "po": "mouth(?)",
        "po'ant": "saliva",
        "po'at": "mouthful(?)",
        "poant": "saliva",
        "pod": "each",
        "poget": "rule",
        "porpa": "king",
        "poru": "(?)",
        "praçiz": "amaze(?)",
        "preniv": "again",
        "prin": "small",
        "proran": "second",
        "præd": "rock",
        "prædec": "rocky",
        "prædnurítí": "money card",
        "prædtígal": "rock-working",
        "præçiz": "amaze(?)",
        "pælmen": "magnet",
        "pælmenec": "magnetic",
        "pæzgo": "fund",
        "pépíl": "be upset(?)",
        "péçavo": "danger",
        "pó": "bulb",
        "púg": "prove(?)",
        "rak": "class(?)",
        "ram": "good",
        "ranal": "various",
        "rasú": "vanquished",
        "rašaþ": "shadow(?)",
        "re'dæntí": "tweezers",
        "rek": "class(?)",
        "relyima": "the Unseen",
        "rem": "flow",
        "rema": "north",
        "remesfet": "diligent",
        "remesfeteþ": "diligence",
        "rifín": "surpass(?)",
        "rifún": "remember",
        "rigabrí": "twenty-two",
        "rigabríec": "twenty-second",
        "rigafa": "twenty-one",
        "rigafaec": "twenty-first",
        "rigasen": "twenty-three",
        "rigasenec": "twenty-third",
        "rigator": "twenty-four",
        "rigatorec": "twenty-fourth",
        "ril": "no",
        "ril'can": "not always",
        "rildil": "nothing",
        "rilnær": "not establish(?)",
        "rilrov": "nobody",
        "riltagamin": "unknown",
        "rilte": "without",
        "rilyima": "unseen",
        "rinto": "coast (?)",
        "rinæltav": "privilege(?)",
        "riš": "twenty",
        "rišec": "twentieth",
        "robot": "actual",
        "ron": "(?)",
        "rotí": "(?)",
        "rov": "person",
        "roçé": "meet(?)",
        "roší": "crater",
        "ráwé": "procedure",
        "rímá": "during(?)",
        "rís": "eat",
        "ríslo": "dissolve",
        "rítan": "(?)",
        "rú": "that",
        "rúb": "but",
        "rúdš": "red",
        "rúmé": "ignore(?)",
        "rún": "zero",
        "rúé": "route",
        "rúék": "destroy",
        "rúéktav": "destruction",
        "saeþ": "own",
        "se": "at",
        "sek": "have",
        "sel": "Write",
        "seltan": "Writer",
        "sen": "three",
        "senec": "third",
        "senaren": "building",
        "set": "us",
        "sev": "age",
        "sex": "have",
        "sifé": "wired",
        "sofegu": "fear",
        "soma": "seal",
        "sova": "(?)",
        "soygi": "stable",
        "stofa": "of one",
        "sé": "design",
        "séra": "west",
        "sín": "get",
        "sógiþ": "stability",
        "t'": "in ",
        "ta": "it(?)",
        "tag": "give",
        "tagam": "know",
        "tagér": "learn",
        "talío": "surface",
        "tam": "fire",
        "taru": "perish(?)",
        "tavo": "15 minutes",
        "te": "with",
        "tefúnet": "memorial",
        "tel": "guild",
        "telbacen": "Guild of Cartographers",
        "telbírí": "Guild of Maintainers",
        "teldú'šol": "Guild of Caterers",
        "telrov": "guildsman",
        "telúk": "Surveyors Guild",
        "telší": "Guild of Messengers",
        "tema": "hear(?)",
        "temo": "in which(?)",
        "ten": "simple",
        "teneš": "simply",
        "ter": "tree",
        "terelin": "contact",
        "tes": "group",
        "tetemo": "within which(?)",
        "tikolít": "sorry",
        "timel": "gallery",
        "tiwa": "shaft",
        "tišma": "friend",
        "to": "place",
        "togaš": "(?)",
        "togo": "floor",
        "tokitu": "determine",
        "tolesæ": "Tolesa",
        "toman": "house",
        "tomana": "home",
        "tome": "homesick",
        "tomet": "here",
        "tomot": "there",
        "tomænæ": "home",
        "tona": "Long",
        "tor": "four",
        "torec": "fourth",
        "toriná": "cold",
        "torn": "spit",
        "trel": "blue",
        "tren": "a few",
        "trom": "wing",
        "tromec": "winged",
        "tænu": "be blind(?)",
        "tænuþ": "blindness(?)",
        "tébun": "(?)",
        "tégan": "love",
        "téní": "welcome",
        "tér": "help",
        "térú": "apparent(?)",
        "térúš": "sensibly(?)",
        "tí'ana": "storyteller",
        "tíg": "work",
        "tígal": "working",
        "tíget": "working",
        "tígtan": "worker",
        "tígtav": "work",
        "tíju": "team(?)",
        "tíma": "south",
        "tíxo": "(?)",
        "túgo": "foot",
        "túl": "grow",
        "túlí": "(?)",
        "túmin": "touched (?)",
        "túní": "(?)",
        "túrí": "(?)",
        "túxút": "(?)",
        "ugrat": "pillar",
        "umt": "(?)",
        "v'ja": "celebration",
        "vagabrí": "seven",
        "vagabríec": "seventh",
        "vagafa": "six",
        "vagafaec": "sixth",
        "vagasen": "eight",
        "vagasenec": "eighth",
        "vagator": "nine",
        "vagatorec": "ninth",
        "vamo": "east",
        "vamot": "eastern",
        "vat": "five",
        "vatec": "fifth",
        "vatí": "(?)",
        "vax": "linking",
        "veren": "hinder(?)",
        "vog": "nature",
        "vogec": "natural",
        "vokæn": "birth",
        "vola": "yes",
        "votana": "truth",
        "votar": "praise",
        "vádu": "tide(?)",
        "válí": "month",
        "váu": "event(?)",
        "vécú": "presence",
        "vénu": "ask(?)",
        "vílé": "soul",
        "víwu": "deserve",
        "víçtav": "acquisition(?)",
        "vúhí": "can",
        "winis": "together(?)",
        "woca": "harsh",
        "xa": "few",
        "xag": "act(?)",
        "xantor": "reflect(?)",
        "xapo": "perhaps",
        "xat": "(?)",
        "xlé": "example",
        "xoyú": "invoke",
        "xæg": "act(?)",
        "xæntor": "reflect(?)",
        "xó": "if(?)",
        "xótag": "result(?)",
        "xótæg": "result(?)",
        "yar": "day",
        "yeret": "may",
        "yim": "see",
        "yima": "seen",
        "yiša": "planet",
        "yípé": "eyeglasses",
        "yíšæ": "Yeesha",
        "yúté": "dedicate(?)",
        "yúté": "guinea pig",
        "zafé": "fate",
        "ze": "him/her",
        "zik": "pod",
        "ziþ": "low",
        "ziþaþ": "least",
        "ziþon": "lower",
        "zo'e": "loss",
        "zu": "end",
        "zunu": "ending",
        "zígla": "mad",
        "zíro": "center",
        "zíwé": "mission(?)",
        "zú": "me",
        "zúdú": "regret",
        "ætinor": "beauty",
        "ætinoret": "beautiful",
        "ætrus": "Atrus",
        "çan": "can(?)",
        "çeto": "ensuing(?)",
        "çev": "thank",
        "çevet": "thankful",
        "çevtavtí": "thanks",
        "çileš": "mainly",
        "çir": "organism",
        "çiso": "archive",
        "çisotan": "archivist",
        "çé": "fault",
        "çólané": "complete",
        "çúr": "learn",
        "éc'dé": "retribution",
        "éla": "(?)",
        "étrus": "Aitrus",
        "éšók": "realize",
        "ín": "any",
        "ír": "bandage",
        "íst": "them",
        "ðelim": "right(?)",
        "ðo": "how",
        "ðozoneš": "however(?)",
        "ðénó": "setback",
        "ón": "myself",
        "úlba": "office",
        "úlin": "control(?)",
        "úlintav": "control(?)",
        "únan": "leadership(?)",
        "únré": "lord",
        "úrú": "community at large",
        "úša": "formula",
        "þoe": "how",
        "šafí": "span",
        "šaverú": "narrow(?)",
        "šela": "(?)",
        "šem": "you",
        "šemtí": "you",
        "šento": "take",
        "šentome": "take from",
        "šeten": "cherish",
        "šin": "able",
        "šokrotan": "bulldozer",
        "šol": "prepare",
        "šolen": "drawn",
        "šora": "peace",
        "šorat": "peaceful",
        "šoxú": "instruct",
        "šufé": "finish",
        "šutíjú": "rocksalt",
        "šíga": "way",
        "šítem": "message",
        "šítemsútan": "messenger",
        "šúga": "(?)",
        "šúþ": "death",
    }

    if dniword in dnidict:
        return dnidict[dniword]
    else:
        return dniword


translation = ""

if args.nts:
    phrase = args.phrase.lower()
else:
    phrase = ots2nts(args.phrase.lower())

phrase = phrase.replace(".", " . ")
phrase = phrase.replace(",", " , ")
phrase = phrase.replace(":", " : ")
phrase = phrase.replace(";", " ; ")
phrase = phrase.replace("!", " ! ")
phrase = phrase.replace("?", " ? ")
phrase = phrase.replace("(", " ( ")
phrase = phrase.replace(")", " ) ")
phrase = phrase.replace("[", " [ ")
phrase = phrase.replace("]", " ] ")
phrase = phrase.replace('"', ' " ')
phrase = phrase.replace("“", " “ ")
phrase = phrase.replace("”", " ” ")
phrase = phrase.replace("’", "'")

phrase = phrase.split(' ')
if args.debug:
    print(">>", phrase, "<<")


negation = 0
passive = 0
condit = 0
genit = 0

for word in phrase:
    if word == " " or word == "":
        continue

    # ARTICLES, CONJUNCTIONS AND PREPOSITIONS

    if (word.startswith("re") or word.startswith("r'")) and word != "re'dæntí" and word != "rek" and word != "relyima" and word != "rem" and word != "rema" and word != "remesfet" and word != "remesfeteþ":
        translation = translation + " the"
        word = word[2:]
    elif word.startswith("bre"):
        translation = translation + " to the"
        word = word[3:]
    elif word.startswith("fre"):
        translation = translation + " at the"
        word = word[3:]
    elif word.startswith("g're") or word.startswith("gre"):
        translation = translation + " and the"
        word = word[3:]
    elif word.startswith("mre"):
        translation = translation + " from the"
        word = word[3:]
    elif word.startswith("tre") and word != "tren":
        translation = translation + " with the"
        word = word[3:]
    elif word.startswith("xre"):
        translation = translation + " for the"
        word = word[3:]

    if word.startswith("erþ"):
        translation = translation + " a"
        word = word[3:]
    elif word.startswith("terþ"):
        translation = translation + " in a"
        word = word[4:]


    if (word.startswith("ga") or word.startswith("g'")) and word != "garkalec" and word != "garísen" and word != "gartavo" and word != "garano" and word != "garkal" and word != "galon" and word != "galpo" and word != "garoš" and word != "garoþ" and word != "garten" and word != "garo" and word != "gan" and word != "gaþ":
        word = word[2:]
        translation = translation + " and"

    if (word.startswith("be") or word.startswith("b'")) and word != "b'ken" and word != "bel" and word != "ben" and word != "bexe":
        word = word[2:]
        translation = translation + " to"

    if (word.startswith("fe") or word.startswith("f'")) and word != "fentasenta" and word != "feltan" and word != "ferem" and word != "fena" and word != "fel":
        word = word[2:]
        translation = translation + " on"

    if (word.startswith("me") or word.startswith("m'")) and word != "megóré" and word != "mepord" and word != "melin" and word != "merk" and word != "meúr" and word != "mer" and word != "mes" and word != "met" and word != "m'la":
        word = word[2:]
        translation = translation + " from"

    if (word.startswith("te") or word.startswith("t'")) and word != "teldú'šol" and word != "telbacen" and word != "tefúnet" and word != "telbírí" and word != "terelin" and word != "telrov" and word != "tetemo" and word != "telší" and word != "telúk" and word != "teneš" and word != "tema" and word != "temo" and word != "tel" and word != "ten" and word != "ter" and word != "tes":
        word = word[2:]
        translation = translation + " with"

    if word.startswith("xe") or word.startswith("x'"):
        word = word[2:]
        translation = translation + " for"

    # GENITIVES

    if word.endswith("ox"):
        word = word[:-2]
        genit = 1
    elif word.startswith("ox"):
        word = word[2:]
        translation = translation + " of "

    if word.endswith("ó") and word != "gestó" and word != "cotó" and word != "ðénó" and word != "pabó" and word != "aró" and word != "pó" and word != "xó":
        word = word[:-1]
        if word.endswith("'"):
            word = word[:-1]
        translation = translation + " my"
    elif word.endswith("om") and word != "trom":
        word = word[:-2]
        if word.endswith("'"):
            word = word[:-1]
        translation = translation + " your"
    elif word.endswith("on") and word != "galon" and word != "muxon" and word != "ziþon" and word != "alon" and word != "elon" and word != "con" and word != "don" and word != "lon" and word != "ron":
        word = word[:-2]
        if word.endswith("'"):
            word = word[:-1]
        translation = translation + " his/her"
    elif word.endswith("ot") and word != "gormot" and word != "h'rot" and word != "robot" and word != "tomot" and word != "vamot" and word != "bot" and word != "mot":
        word = word[:-2]
        if word.endswith("'"):
            word = word[:-1]
        translation = translation + " our"
    elif word.endswith("omí"):
        word = word[:-3]
        if word.endswith("'"):
            word = word[:-1]
        translation = translation + " your"
    elif word.endswith("os"):
        word = word[:-2]
        if word.endswith("'"):
            word = word[:-1]
        translation = translation + " their"

    # CHECK FOR NEGATION

    if word == "ril":
        negation = 1
        continue

    # CHECK FOR CONDITIONALS

    if word == "kenen":
        condit = 1
        continue
    if condit == 1:
        if word == "vúhí":
            translation = translation + " could be"
            condit = 0
            continue
        else:
            translation = translation + " is"
            condit = 0

    # CHECK FOR PASSIVES

    if word.endswith("ij"):
        passive = 1
        word = word[:-2]
        continue

    # FUTURE PERFECT PROGRESSIVE

    if word.startswith("bodol"):
        if negation == 1:
            mood = "will not have been "
            negation = 0
        else:
            mood = "will have been "
        if passive == 1:
            ending = "en"
            mood = mood + "being "
            passive = 0
        else:
            ending = "ing"
        word = word[5:]

        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("en") and word != "kenen" and word != "garten":
            word = word[:-2]
            translation = translation + " (s/he) " + mood + translate(word) + ending
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + ending
        elif word.endswith("tí") and word != "bæntí" and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + ending
        else:
            translation = translation + " I "      + mood + translate(word) + ending

        if translation.endswith("een"):
            translation = translation[:-3]
            translation = translation + "en"
        continue

    # FUTURE PROGRESSIVE

    elif word.startswith("bodo"):
        if negation == 1:
            mood = "will not be "
            negation = 0
        else:
            mood = "will be "
        if passive == 1:
            ending = "en"
            mood = mood + "being "
            passive = 0
        else:
            ending = "ing"
        word = word[4:]

        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("en") and word != "kenen" and word != "garten" and word != "sen":
            word = word[:-2]
            translation = translation + " (s/he) " + mood + translate(word) + ending
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + ending
        elif word.endswith("tí") and word != "bæntí" and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + ending
        else:
            translation = translation + " I "      + mood + translate(word) + ending

        if translation.endswith("een"):
            translation = translation[:-3]
            translation = translation + "en"
        continue

    # FUTURE PERFECT

    elif word.startswith("boko"):
        if negation == 1:
            mood = "will not have "
            negation = 0
        else:
            mood = "will have "
        if passive == 1:
            ending = "en"
            mood = mood + "been "
            passive = 0
        else:
            ending = "en"
        word = word[4:]

        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("en") and word != "kenen" and word != "garten":
            word = word[:-2]
            translation = translation + " (s/he) " + mood + translate(word) + ending
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + ending
        elif word.endswith("tí") and word != "bæntí" and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + ending
        else:
            translation = translation + " I "      + mood + translate(word) + ending

        if translation.endswith("een"):
            translation = translation[:-3]
            translation = translation + "en"
        continue

    # FUTURE PERFECT, ALTERN. FORM

    elif word.startswith("bol"):
        if negation == 1:
            mood = "will not have "
            negation = 0
        else:
            mood = "will have "
        if passive == 1:
            ending = "en"
            mood = mood + "been "
            passive = 0
        else:
            ending = "en"
        word = word[3:]

        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("en") and word != "kenen" and word != "garten":
            word = word[:-2]
            translation = translation + " (s/he) " + mood + translate(word) + ending
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + ending
        elif word.endswith("tí") and word != "bæntí" and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + ending
        else:
            translation = translation + " I "      + mood + translate(word) + ending

        if translation.endswith("een"):
            translation = translation[:-3]
            translation = translation + "en"
        continue

    # SIMPLE FUTURE

    elif word.startswith("bo") and not word.startswith("boken") and word != "bonú" and word != "bonúec" and word != "borta" and word != "bot":
        if negation == 1:
            mood = "will not "
            negation = 0
        else:
            mood = "will "
        if passive == 1:
            ending = "en"
            mood = mood + "be "
            passive = 0
        else:
            ending = ""
        word = word[2:]

        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("en") and word != "kenen" and word != "garten":
            word = word[:-2]
            translation = translation + " (s/he) " + mood + translate(word) + ending
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + ending
        elif word.endswith("tí") and word != "bæntí" and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + ending
        elif word != "ken":
            translation = translation + " I "      + mood + translate(word) + ending

        if translation.endswith("een"):
            translation = translation[:-3]
            translation = translation + "en"
        continue

    # FUTURE PERFECT CONDITIONAL

    elif word.startswith("kobol"):
        if negation == 1:
            mood = "would not have "
            negation = 0
        else:
            mood = "would have "
        if passive == 1:
            ending = "en"
            mood = mood + "been "
            passive = 0
        else:
            ending = "ed"
        word = word[5:]

        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("en") and word != "kenen" and word != "garten":
            word = word[:-2]
            translation = translation + " (s/he) " + mood + translate(word) + ending
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + ending
        elif word.endswith("tí") and word != "bæntí" and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + ending
        elif word != "ken":
            translation = translation + " I "      + mood + translate(word) + ending

        if translation.endswith("eed"):
            translation = translation[:-3]
            translation = translation + "ed"
        elif translation.endswith("een"):
            translation = translation[:-3]
            translation = translation + "en"
        continue

    # PAST PERFECT PROGRESSIVE

    elif word.startswith("kodol"):
        if negation == 1:
            mood = "have not been "
            negation = 0
        else:
            mood = "have been "
        if passive == 1:
            ending = "ed"
            mood = mood + "being "
            passive = 0
        else:
            ending = "ing"
        word = word[5:]

        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("en") and word != "kenen" and word != "garten":
            word = word[:-2]
            mood = mood.replace("have", "has")
            translation = translation + " (s/he) " + mood + translate(word) + ending
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + ending
        elif word.endswith("tí") and word != "bæntí" and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + ending
        elif word != "ken":
            translation = translation + " I "      + mood + translate(word) + ending

        if translation.endswith("eed"):
            translation = translation[:-3]
            translation = translation + "ed"
        continue

    # PAST PROGRESSIVE

    elif word.startswith("kodo"):
        if negation == 1:
            mood = "were not "
            negation = 0
        else:
            mood = "were "
        if passive == 1:
            ending = "ed"
            mood = mood + "being "
            passive = 0
        else:
            ending = "ing"
        word = word[4:]

        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("en") and word != "kenen" and word != "garten":
            word = word[:-2]
            mood = mood.replace("were", "was")
            translation = translation + " (s/he) " + mood + translate(word) + ending
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + ending
        elif word.endswith("tí") and word != "bæntí" and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + ending
        elif word != "ken":
            mood = mood.replace("were", "was")
            translation = translation + " I "      + mood + translate(word) + ending

        if translation.endswith("eed"):
            translation = translation[:-3]
            translation = translation + "ed"
        continue

    # PAST PERFECT

    elif word.startswith("kol"):
        if negation == 1:
            mood = "had not "
            negation = 0
        else:
            mood = "had "
        if passive == 1:
            ending = "ed"
            mood = mood + "been "
            passive = 0
        else:
            ending = "ed"
        word = word[3:]

        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("en") and word != "kenen" and word != "garten":
            word = word[:-2]
            translation = translation + " (s/he) " + mood + translate(word) + ending
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + ending
        elif word.endswith("tí") and word != "bæntí" and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + ending
        elif word != "ken":
            translation = translation + " I "      + mood + translate(word) + ending

        if translation.endswith("eed"):
            translation = translation[:-3]
            translation = translation + "ed"
        continue

    # SIMPLE PAST

    elif word.startswith("ko") and not word.startswith("koken") and word != "kor'nía" and word != "kor'vax" and word != "korman" and word != "korvax" and word != "korfa" and word != "koca" and word != "kota" and word != "kor":
        word = word[2:]
        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            if negation == 1:
                if passive == 1:
                    translation = translation + " you weren't "    + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " you didn't "     + translate(word)
                negation = 0
            else:
                if passive == 1:
                    translation = translation + " you were "       + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " you "            + translate(word) + "ed"
        elif word.endswith("en") and word != "kenen" and word != "garten":
            word = word[:-2]
            if negation == 1:
                if passive == 1:
                    translation = translation + " (s/he) wasn't "  + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " (s/he) didn't "  + translate(word)
                negation = 0
            else:
                if passive == 1:
                    translation = translation + " (s/he) was "     + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " (s/he) "         + translate(word) + "ed"
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            if negation == 1:
                if passive == 1:
                    translation = translation + " we weren't "     + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " we didn't "      + translate(word)
                negation = 0
            else:
                if passive == 1:
                    translation = translation + " we were "        + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " we "             + translate(word) + "ed"
        elif word.endswith("tí") and word != "bæntí" and word != "kentí":
            word = word[:-2]
            if negation == 1:
                if passive == 1:
                    translation = translation + " you weren't "    + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " you didn't "     + translate(word)
                negation = 0
            else:
                if passive == 1:
                    translation = translation + " you were "       + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " you "            + translate(word) + "ed"
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            if negation == 1:
                if passive == 1:
                    translation = translation + " (they) weren't " + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " (they) didn't "  + translate(word)
                negation = 0
            else:
                if passive == 1:
                    translation = translation + " (they) were "    + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " (they) "         + translate(word) + "ed"
        elif word != "ken":
            word = word[:-2]
            if negation == 1:
                if passive == 1:
                    translation = translation + " I wasn't "       + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " I didn't "       + translate(word)
                negation = 0
            else:
                if passive == 1:
                    translation = translation + " I was "          + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " I "              + translate(word) + "ed"

        if translation.endswith("eed"):
            translation = translation[:-3]
            translation = translation + "ed"
        continue

    # PRESENT PERFECT PROGRESSIVE (and passive, but not checked for)

    elif word.startswith("dol"):
        if negation == 1:
            mood = "have not been "
            negation = 0
        else:
            mood = "have been "
        word = word[3:]
        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "ing"
        elif word.endswith("en") and word != "kenen" and word != "garten":
            word = word[:-2]
            mood = mood.replace("have", "has")
            translation = translation + " (s/he) " + mood + translate(word) + "ing"
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + "ing"
        elif word.endswith("tí") and word != "bæntí" and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "ing"
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + "ing"
        elif word != "ken":
            translation = translation + " I "      + mood + translate(word) + "ing"
        continue

    # PRESENT PROGRESSIVE

    elif word.startswith("do") and not word.startswith("dormað") and word != "doren" and word != "dova" and word != "don":
        word = word[2:]
        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            if negation == 1:
                if passive == 1:
                    translation = translation + " you aren't being "    + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " you aren't "          + translate(word) + "ing"
                negation = 0
            else:
                if passive == 1:
                    translation = translation + " you are being "       + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " you are"              + translate(word) + "ing"
        elif word.endswith("en") and word != "kenen" and word != "garten":
            word = word[:-2]
            if negation == 1:
                if passive == 1:
                    translation = translation + " (s/he) isn't being "  + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " (s/he) isn't "        + translate(word) + "ing"
                negation = 0
            else:
                if passive == 1:
                    translation = translation + " (s/he) is being "     + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " (s/he) is "           + translate(word) + "ing"
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            if negation == 1:
                if passive == 1:
                    translation = translation + " we aren't being "     + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " we aren't "           + translate(word) + "ing"
                negation = 0
            else:
                if passive == 1:
                    translation = translation + " we are being "        + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " we are "              + translate(word) + "ing"
        elif word.endswith("tí") and word != "bæntí" and word != "kentí":
            word = word[:-2]
            if negation == 1:
                if passive == 1:
                    translation = translation + " you aren't being "    + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " you aren't "          + translate(word) + "ing"
                negation = 0
            else:
                if passive == 1:
                    translation = translation + " you are being "       + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " you are "             + translate(word) + "ing"
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            if negation == 1:
                if passive == 1:
                    translation = translation + " (they) aren't being " + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " (they) aren't "       + translate(word) + "ing"
                negation = 0
            else:
                if passive == 1:
                    translation = translation + " (they) are being "    + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " (they) are "              + translate(word) + "ing"
        elif word != "ken":
            word = word[:-2]
            if negation == 1:
                if passive == 1:
                    translation = translation + " I'm not being "       + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " I'm not "             + translate(word) + "ing"
                negation = 0
            else:
                if passive == 1:
                    translation = translation + " I'm being "           + translate(word) + "ed"
                    passive = 0
                else:
                    translation = translation + " I'm "                 + translate(word) + "ing"
        continue

    # PRESENT PERFECT

    elif (word.startswith("le") or word.startswith("l'")) and word != "lem" and word != "lena" and word != "lenita" and word != "lesa" and word != "leš":
        if negation == 1:
            mood = "have not "
            negation = 0
        else:
            mood = "have "
        if passive == 1:
            ending = "en"
            mood = mood + "been "
            passive = 0
        else:
            ending = "en"
        word = word[2:]

        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("en") and word != "kenen" and word != "garten":
            word = word[:-2]
            mood = mood.replace("have", "has")
            translation = translation + " (s/he) " + mood + translate(word) + ending
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + ending
        elif word.endswith("tí") and word != "bæntí" and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + ending
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + ending
        elif word != "ken":
            translation = translation + " I "      + mood + translate(word) + ending

        if translation.endswith("een"):
            translation = translation[:-3]
            translation = translation + "en"
        if translation.endswith("beginen"):
            translation = translation[:-7]
            translation = translation + "begun"
        continue

    # SIMPLE PRESENT

    if word.endswith("em") and word != "rem" and not word.endswith("kenem"):
        word = word[:-2]
        if passive == 1:
            translation = translation + " are " + translate(word) + "ed"
            passive = 0
        else:
            translation = translation + " " + translate(word)
        continue
    elif word.endswith("en") and word != "sen" and word != "ten" and word != "tren" and word != "garten" and word != "kílen" and not word.endswith("kenen") and not word.endswith("ken"):
        word = word[:-2]
        if translation.endswith("can"):
            translation = translation + " " + translate(word)
        else:
            if passive == 1:
                translation = translation + " are " + translate(word) + "ed"
                passive = 0
            else:
                translation = translation + " " + translate(word) + "s"
        continue
    elif word.endswith("et") and not word.endswith("kenet"):
        word = word[:-2]
        if passive == 1:
            translation = translation + " are " + translate(word) + "ed"
            passive = 0
        else:
            translation = translation + " " + translate(word)
        continue
    elif word.endswith("tí") and word != "bæntí" and not word.endswith("kentí"):
        if word == "cotótí" or word == "šemtí":
            translation = translation + " " + translate(word)
        else:
            word = word[:-2]
            if passive == 1:
                translation = translation + " are " + translate(word) + "ed"
                passive = 0
            else:
                translation = translation + " " + translate(word) + "s"
        continue
    elif word.endswith("ít") and not word.endswith("kenít"):
        word = word[:-2]
        if passive == 1:
            translation = translation + " are " + translate(word) + "ed"
            passive = 0
        else:
            translation = translation + " " + translate(word)
        continue

    # MODIFIERS

    if word.endswith("tan") and word != "arotan" and word != "aríutan" and word != "bacentan" and word != "bareltan" and word != "entan" and word != "golantan" and word != "kantintan" and word != "lésútan" and word != "marntan" and word != "matan" and word != "rítan" and word != "çisotan" and word != "šokrotan" and word != "šítemsútan":
        word = word[:-3]
        translation = translation + " " + translate(word) + "er"
        if translation.endswith("eer"):
            translation = translation[:-3]
            translation = translation + "er"
        continue

    elif word.endswith("tav") and word != "bareltav" and word != "cosatav" and word != "fúsatav" and word != "geltav" and word != "inæltav" and word != "kesotav" and word != "keštav" and word != "manšútav" and word != "místav" and word != "nudatav" and word != "rinæltav" and word != "rúéktav" and word != "tígtav" and word != "víçtav" and word != "úlintav":
        word = word[:-3]
        translation = translation + " " + translate(word) + "ion"
        if translation.endswith("eion"):
            translation = translation[:-4]
            translation = translation + "ion"
        continue

    elif word.endswith("aloþ") and word != "kantinaloþ" and word != "nekisaloþ" and word != "enyaloþ":
        word = word[:-4]
        translation = translation + " " + translate(word) + "er"
        if translation.endswith("eer"):
            translation = translation[:-3]
            translation = translation + "er"
        continue

    elif word.endswith("am") and word != "anotam" and word != "datam" and word != "fam" and word != "líam" and word != "pam" and word != "ram" and word != "tagam" and word != "tam":
        word = word[:-2]
        translation = translation + " " + translate(word) + "-member"
        continue

    elif word.endswith("ec") and word != "abcíec" and word != "anoec" and word != "bonúec" and word != "garkalec" and word != "nadanec" and word != "prædec" and word != "pælmenec" and word != "tromec" and not word.endswith("faec") and not word.endswith("bríec") and not word.endswith("senec") and not word.endswith("torec") and not word.endswith("vatec") and not word.endswith("névúec") and not word.endswith("híborec") and not word.endswith("rišec") and not word.endswith("fasíec"):
        word = word[:-2]
        translation = translation + " " + translate(word) + "y"
        continue

    elif word.endswith("et") and word != "baronet" and word != "bokenet" and word != "elonet" and word != "gormet" and word != "kenet" and word != "kokenet" and word != "met" and word != "poget" and word != "remesfet" and word != "set" and word != "tefúnet" and word != "tomet" and word != "tíget" and word != "yeret" and word != "ætinoret" and word != "çevet":
        word = word[:-2]
        translation = translation + " " + translate(word) + "ful"
        continue

    elif word.endswith("eš") and word != "k'teš" and word != "kageš" and word != "leš" and word != "mileš" and word != "nígeš" and word != "teneš" and word != "çileš" and word != "ðozoneš":
        word = word[:-2]
        translation = translation + " " + translate(word) + "ly"
        continue

    # MISC

    if word.endswith("nava"):
        word = word[:-4]
        translation = translation + " " + translate(word) + " Master"
        continue

    # NUMBERS

    if word.endswith("sí") and word != "fasí":
        word = word[:-2]
        translation = translation + " " + translate(word) + " times 25"
        continue
    elif word.endswith("ra") and word != "bíra" and word != "gera" and word != "gira" and word != "kera" and word != "para" and word != "séra" and word != "šora":
        word = word[:-2]
        translation = translation + " " + translate(word) + " times 25^2"
        continue
    elif (word.endswith("lan") or word.endswith("len")) and word != "emelan" and word != "lan" and word != "oglan" and word != "kílen" and word != "šolen":
        word = word[:-2]
        translation = translation + " " + translate(word) + " times 25^3"
        continue
    elif word.endswith("mel") and word != "timel":
        word = word[:-2]
        translation = translation + " " + translate(word) + " times 25^4"
        continue
    elif word.endswith("blo") and word != "blo":
        word = word[:-2]
        translation = translation + " " + translate(word) + " times 25^5"
        continue

    # PRESENT PARTICIPLE

    if word.endswith("al") and word != "coidal" and word != "cogal" and word != "címaal" and word != "garkal" and word != "nekisal" and word != "cogal" and word != "pal" and word != "prædtígal" and word != "tígal":
        word = word[:-2]
        translation = translation + " " + translate(word) + "ing"
        continue

    # PAST PARTICIPLE

    if word.endswith("in") and word != "bavanin" and word != "búgin" and word != "delin" and word != "flin" and word != "bavanin" and word != "bavanin" and word != "bavanin":
        word = word[:-2]
        translation = translation + " " + translate(word) + "ed"
        if translation.endswith("eed"):
            translation = translation[:-3]
            translation = translation + "ed"
        continue

    # NEGATION, NOT IN VERBAL CONTEXT

    if negation == 1:
        translation = translation + " no(t) " + translate(word)
        negation = 0
    elif genit == 1:
        translation = translation + " " + translate(word) + " of"
        genit = 0
    else:
        translation = translation + " " + translate(word)


#    engword = engword.replace("-þ", "ty")
#    engword = engword.replace("-š", "ly")

#    engword = engword.replace("d'", "again-")
#    engword = engword.replace("de-", "again")

print(translation)

