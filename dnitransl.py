#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
from argparse import RawTextHelpFormatter

parser = argparse.ArgumentParser(description="""
Attempts a very rough translation of a D'ni sentence.

Examples:

dnitransl.py ".xapo rezunu rildolgelenij gaþ"
"..."

dnitransl.py -o ".khahpo rehzuhnuh rildolgehlehnij gahth"
"..."
""", formatter_class=RawTextHelpFormatter)

parser.add_argument("-o", "--ots", action='store_true', help="Old Transliteration Standard")
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
        "manšútavting": "mortality(?)",
        "fentasenta": "historian",
        "kantinaloþ": "oppressed(?)",
        "mor'ox'mor": "grandmother",
        "mor'ox'por": "grandmother(?)",
        "mor’ox’mor": "grandmother",
        "mor’ox’por": "grandmother(?)",
        "prædnurítí": "money card",
        "remesfeteþ": "diligence",
        "riltagamin": "unknown",
        "šítemsútan": "messenger",
        "dú'šoltan": "caterer",
        "dú’šoltan": "caterer",
        "kantintan": "oppressor(?)",
        "næ'grenis": "brittle",
        "næ’grenis": "brittle",
        "nekisaloþ": "bent",
        "prædtígal": "rock-working",
        "teldú'šol": "Guild of Caterers",
        "teldú’šol": "Guild of Caterers",
        "ætinoret": "beautiful",
        "azmorelu": "Osmorella(?)",
        "bacentan": "cartographer",
        "bareltan": "God",
        "bareltav": "made",
        "çevtavtí": "thanks",
        "garkalec": "stormy",
        "golantan": "judge",
        "manšútav": "death",
        "mištatav": "construction",
        "moroxmor": "grandmother",
        "moroxpor": "grandmother(?)",
        "pælmenec": "magnetic",
        "re'dæntí": "tweezers",
        "re’dæntí": "tweezers",
        "remesfet": "diligent",
        "rinæltav": "privilege(?)",
        "šokrotan": "bulldozer",
        "telbacen": "Guild of Cartographers",
        "aríutan": "protector",
        "aríutav": "protection",
        "bantano": "island",
        "baronet": "phosphorescent",
        "bavanin": "hidden(?)",
        "bokenem": "you will be",
        "bokenen": "s/he will be",
        "bokenet": "we will be",
        "bokentí": "you will be",
        "bokenít": "they will be",
        "bírítan": "maintainer",
        "çisotan": "archivist",
        "cosatav": "possession(?)",
        "devokæn": "hope",
        "ðozoneš": "however(?)",
        "elíaniþ": "upper class(?)",
        "endétan": "builder",
        "enyaloþ": "sickly",
        "fúsatav": "name",
        "garísen": "garrison",
        "gartavo": "6 hours",
        "gorayæn": "clock",
        "hígabrí": "seventeen",
        "hígasen": "eighteen",
        "hígator": "nineteen",
        "iglarno": "temporary",
        "inæltav": "opportunity(?)",
        "kesotan": "changer",
        "kesotav": "change",
        "kokenem": "were",
        "kokenen": "was",
        "kokenet": "were",
        "kokentí": "were",
        "kokenít": "were",
        "kor'nía": "Blank Book",
        "kor’nía": "Blank Book",
        "kor'vax": "Linking Book",
        "kor’vax": "Linking Book",
        "lésútan": "carrier",
        "marntan": "creator",
        "marntav": "creation",
        "maryéša": "fan(?)",
        "nadanec": "mushroomy",
        "négabrí": "twelve",
        "négasen": "thirteen",
        "négator": "fourteen",
        "nekisal": "bent",
        "nudatav": "disaster(?)",
        "partavo": "hour",
        "relyima": "the Unseen",
        "rigabrí": "twenty-two",
        "rigasen": "twenty-three",
        "rigator": "twenty-four",
        "rilyima": "unseen",
        "rúéktav": "destruction",
        "senaren": "building",
        "šentome": "take from",
        "tefúnet": "memorial",
        "telbírí": "Guild of Maintainers",
        "terelin": "contact",
        "tikolít": "sorry",
        "úlintav": "control(?)",
        "vagabrí": "seven",
        "vagasen": "eight",
        "vagator": "nine",
        "abcíec": "basaltic",
        "ætinor": "beauty",
        "anotam": "lava",
        "arotan": "outsider",
        "bacana": "map",
        "bivdil": "everything",
        "bivrov": "everyone",
        "bonúec": "acidic",
        "canril": "never",
        "címaal": "needed",
        "coidal": "glowing",
        "çólané": "complete",
        "cotótí": "children",
        "desíké": "puzzle",
        "dormað": "defeat",
        "dratol": "(?)",
        "dú'šol": "cater",
        "dú’šol": "cater",
        "elemar": "spore",
        "elonet": "uplifting(?)",
        "emelan": "(?)",
        "enyælo": "sick",
        "feltan": "rower",
        "garano": "ocean",
        "garkal": "storm",
        "ge'dan": "wisdom",
        "ge’dan": "wisdom",
        "geltan": "writer",
        "geltav": "writings",
        "gerano": "foundation(?)",
        "gidtav": "excavation",
        "gormet": "now",
        "gormot": "then",
        "gorven": "soon",
        "graner": "circle(?)",
        "harten": "wait(?)",
        "hevkor": "lexicon",
        "hígafa": "sixteen",
        "húsaté": "satisfied(?)",
        "kæligo": "council",
        "kæmdol": "why",
        "kæmrov": "who",
        "kanhag": "(?)",
        "kanræd": "think",
        "kantin": "oppress(?)",
        "kelaní": "antelope",
        "keštav": "warning",
        "korman": "Descriptive Book",
        "korvax": "Linking Book",
        "lenita": "idiot",
        "líaniþ": "division(?)",
        "manšúþ": "death-bringer",
        "marent": "follow",
        "megóré": "straight out",
        "mepord": "(?)",
        "místan": "speaker",
        "místav": "speech",
        "négafa": "eleven",
        "nícavé": "suffer",
        "oenazo": "hope",
        "omšíno": "(?)",
        "ošanin": "lost",
        "pælmen": "magnet",
        "parano": "sea(?)",
        "péçavo": "danger",
        "po'ant": "saliva",
        "po’ant": "saliva",
        "praçiz": "amaze(?)",
        "præçiz": "amaze(?)",
        "prædec": "rocky",
        "preniv": "again",
        "proran": "second",
        "rigafa": "twenty-one",
        "rildil": "nothing",
        "rilnær": "not establish(?)",
        "rilrov": "nobody",
        "šaverú": "narrow(?)",
        "seltan": "Writer",
        "sofegu": "fear",
        "šutíjú": "rocksalt",
        "telrov": "guildsman",
        "tetemo": "within which(?)",
        "tí'ana": "storyteller",
        "tí’ana": "storyteller",
        "tígtan": "worker",
        "tígtav": "work",
        "tokitu": "determine",
        "tomana": "home",
        "toriná": "cold",
        "tromec": "winged",
        "vagafa": "six",
        "víçtav": "acquisition(?)",
        "votana": "truth",
        "xæntor": "reflect(?)",
        "xantor": "reflect(?)",
        "anoec": "wet",
        "ba'ro": "bahro",
        "ba’ro": "bahro",
        "bacen": "map",
        "bæntí": "series",
        "barel": "make",
        "barta": "accomplish(?)",
        "bigto": "blessing",
        "biran": "sea(?)",
        "bišta": "tunnel",
        "b'ken": "to be",
        "b’ken": "to be",
        "borta": "purpose(?)",
        "búgin": "creature",
        "bugšo": "(?)",
        "canoš": "permanently",
        "cavan": "immortal",
        "cédor": "(?)",
        "çevet": "thankful",
        "çileš": "mainly",
        "cogal": "sunny",
        "da'ko": "marble",
        "da’ko": "marble",
        "daban": "alembic(?)",
        "datam": "firemarble",
        "ðelim": "right(?)",
        "delin": "mist",
        "doren": "(?)",
        "éc'dé": "retribution",
        "éc’dé": "retribution",
        "elían": "upper class(?)",
        "entan": "honesty(?)",
        "ferem": "dry",
        "filað": "top",
        "foles": "watch(?)",
        "foršu": "(?)",
        "galon": "ground",
        "galpo": "cave",
        "garoš": "greatly",
        "garoþ": "greatness",
        "geran": "foundation(?)",
        "gestó": "Art",
        "gicaþ": "safety",
        "gimit": "immediate",
        "gonaþ": "poor(?)",
        "goran": "30 seconds",
        "gulem": "strait(?)",
        "h'rot": "(?)",
        "h’rot": "(?)",
        "híbor": "fifteen",
        "húcéþ": "benevolence(?)",
        "ilæis": "power",
        "irvæn": "mineral",
        "isyír": "revere",
        "jakúþ": "Devil",
        "jerúþ": "possibility",
        "k'teš": "entertain",
        "k’teš": "entertain",
        "kæmfa": "which",
        "kæmto": "where",
        "kageš": "originally",
        "boken": "I will be",
        "kenem": "you are",
        "kenet": "we are",
        "kentí": "you are",
        "kenít": "are",
        "keraþ": "Brave One",
        "kevoþ": "another",
        "kílen": "step",
        "kirin": "desert sand",
        "koken": "I was",
        "korfa": "First Book",
        "líšan": "whole",
        "lómat": "though",
        "lonep": "discovery(?)",
        "loræg": "grace(?)",
        "lorag": "grace(?)",
        "mægen": "powers(?)",
        "magen": "powers(?)",
        "manšú": "die",
        "matan": "leave(?)",
        "melin": "outer",
        "mileš": "overwhelm(?)",
        "mišta": "construct",
        "morpa": "queen",
        "múden": "fortune",
        "muxon": "complex",
        "nadan": "mushroom",
        "nefex": "(?)",
        "nekis": "bend",
        "nesít": "(?)",
        "nesít": "(?)",
        "nígeš": "merely",
        "nogin": "ignore(?)",
        "noref": "final",
        "oglan": "ancient",
        "pæzgo": "fund",
        "paraþ": "greatness",
        "pelúl": "(?)",
        "pépíl": "be upset(?)",
        "peraþ": "(?)",
        "pilel": "receive",
        "pirin": "rubbed(?)",
        "po'at": "mouthful(?)",
        "po’at": "mouthful(?)",
        "poant": "saliva",
        "poget": "rule",
        "porpa": "king",
        "ranal": "various",
        "rašaþ": "shadow(?)",
        "rifín": "surpass(?)",
        "rifún": "remember",
        "rilte": "without",
        "rinto": "coast (?)",
        "ríslo": "dissolve",
        "rítan": "(?)",
        "robot": "actual",
        "šemtí": "you",
        "šento": "take",
        "šeten": "cherish",
        "šítem": "message",
        "sógiþ": "stability",
        "šolen": "drawn",
        "šorat": "peaceful",
        "soygi": "stable",
        "stofa": "of one",
        "tænuþ": "blindness(?)",
        "tagam": "know",
        "tagér": "learn",
        "talío": "surface",
        "tébun": "(?)",
        "tégan": "love",
        "telší": "Guild of Messengers",
        "telúk": "Surveyors Guild",
        "teneš": "simply",
        "térúš": "sensibly(?)",
        "tígal": "working",
        "tíget": "working",
        "timel": "gallery",
        "tišma": "friend",
        "togaš": "(?)",
        "toman": "house",
        "tomet": "here",
        "tomot": "there",
        "torec": "fourth",
        "túmin": "touched (?)",
        "túxút": "(?)",
        "ugrat": "pillar",
        "vamot": "eastern",
        "veren": "hinder(?)",
        "vogec": "natural",
        "vokæn": "birth",
        "votar": "praise",
        "winis": "together(?)",
        "xótæg": "result(?)",
        "xótag": "result(?)",
        "yeret": "may",
        "zígla": "mad",
        "ziþaþ": "least",
        "ziþon": "lower",
        "abcí": "basalt",
        "alga": "(?)",
        "aríu": "protect",
        "arta": "do(?)",
        "atmé": "stop(?)",
        "baro": "bahro",
        "bexe": "compel",
        "bíra": "keep",
        "bírí": "maintain",
        "bonú": "acid",
        "brún": "tube",
        "cano": "everlasting",
        "carú": "full(?)",
        "çeto": "ensuing(?)",
        "chil": "main",
        "címa": "need",
        "çiso": "archive",
        "cofa": "horn",
        "coid": "glow",
        "cotó": "child",
        "cúnú": "greet",
        "cúté": "guinea pig",
        "dako": "marble",
        "déjí": "path",
        "ðénó": "setback",
        "dóha": "machine",
        "dova": "world",
        "eder": "rest",
        "elaþ": "highest ones(?)",
        "elaþ": "elite(?)",
        "elon": "raise(?)",
        "endé": "build",
        "erem": "skill",
        "éšók": "realize",
        "etaf": "(?)",
        "faðo": "experience",
        "faex": "first",
        "fala": "fold",
        "fasí": "twenty-five",
        "fena": "story",
        "fité": "look(?)",
        "flin": "order",
        "fúru": "sufficient",
        "fúsa": "call",
        "gæta": "due",
        "garo": "great",
        "gedí": "surprise(?)",
        "gera": "center(?)",
        "gica": "safe",
        "gilo": "plant",
        "gira": "steam(?)",
        "glas": "drink",
        "gola": "justice(?)",
        "gopa": "because",
        "góré": "straight",
        "hapo": "combine",
        "haza": "white",
        "hern": "room",
        "hevo": "swarm",
        "iðsé": "line",
        "jaga": "warrant(?)",
        "jerú": "possible",
        "jima": "prophecy",
        "jixa": "remain(?)",
        "k'cí": "happy",
        "k’cí": "happy",
        "kazí": "detour",
        "kera": "brave",
        "keso": "change",
        "kevo": "another",
        "kíba": "obey",
        "kíla": "endure(?)",
        "kino": "surrender(?)",
        "kiri": "krill fly(?)",
        "koca": "gate",
        "kota": "locked door",
        "kúan": "stream",
        "kúza": "depart(?)",
        "lasa": "seal",
        "lena": "journey",
        "lesa": "sealed",
        "lésú": "carry",
        "líam": "part(?)",
        "líša": "whole(?)",
        "lúpa": "precaution(?)",
        "m'la": "lizard",
        "m’la": "lizard",
        "maðo": "succeed(?)",
        "mæðo": "succeed(?)",
        "mælo": "forget",
        "mala": "come",
        "marg": "layer",
        "marn": "create",
        "máru": "desire(?)",
        "máúd": "means(?)",
        "merk": "poisoned water",
        "meúr": "you're welcome",
        "miro": "toxic",
        "mišo": "universe",
        "motí": "those",
        "múší": "invention(?)",
        "nava": "master",
        "nagé": "learn(?)",
        "naga": "learn(?)",
        "névú": "ten",
        "neze": "read",
        "ogel": "age(?)",
        "olíx": "(?)",
        "oner": "just",
        "ošan": "lose",
        "pabó": "bless",
        "para": "great",
        "parx": "pray(?)",
        "peké": "equal(?)",
        "pišo": "belong",
        "poru": "(?)",
        "præd": "rock",
        "prin": "small",
        "rasú": "vanquished",
        "ráwé": "procedure",
        "rema": "north",
        "rímá": "during(?)",
        "roçé": "meet(?)",
        "roší": "crater",
        "rotí": "(?)",
        "rúdš": "red",
        "rúék": "destroy",
        "rúmé": "ignore(?)",
        "saeþ": "own",
        "šafí": "span",
        "šela": "(?)",
        "séra": "west",
        "sifé": "wired",
        "šíga": "way",
        "soma": "seal",
        "šora": "peace",
        "sova": "(?)",
        "šoxú": "instruct",
        "šufé": "finish",
        "šúga": "(?)",
        "tænu": "be blind(?)",
        "taru": "perish(?)",
        "tavo": "15 minutes",
        "tema": "hear(?)",
        "temo": "in which(?)",
        "téní": "welcome",
        "térú": "apparent(?)",
        "tíju": "team(?)",
        "tíma": "south",
        "tiwa": "shaft",
        "tíxo": "(?)",
        "togo": "floor",
        "tome": "homesick",
        "tona": "Long",
        "torn": "spit",
        "trel": "blue",
        "tren": "a few",
        "trom": "wing",
        "túgo": "foot",
        "túlí": "(?)",
        "túní": "(?)",
        "túrí": "(?)",
        "úlba": "office",
        "úlin": "control(?)",
        "únan": "leadership(?)",
        "únré": "lord",
        "v'ja": "celebration",
        "v’ja": "celebration",
        "vádu": "tide(?)",
        "válí": "month",
        "vamo": "east",
        "vatí": "(?)",
        "vécú": "presence",
        "vénu": "ask(?)",
        "vílé": "soul",
        "víwu": "deserve",
        "vola": "yes",
        "vúhí": "can",
        "woca": "harsh",
        "xapo": "perhaps",
        "xoyú": "invoke",
        "yima": "seen",
        "yípé": "eyeglasses",
        "yiša": "planet",
        "yúté": "guinea pig",
        "yúté": "dedicate(?)",
        "zafé": "fate",
        "zíro": "center",
        "zíwé": "mission(?)",
        "zo'e": "loss",
        "zo’e": "loss",
        "zúdú": "regret",
        "zunu": "ending",
        "aça": "light(?)",
        "acú": "ready",
        "ago": "well",
        "aní": "become",
        "ano": "water",
        "aro": "other",
        "aró": "attend(?)",
        "ave": "error",
        "avo": "Father(?)",
        "bæš": "sense(?)",
        "bar": "(?)",
        "baš": "sense(?)",
        "bel": "claim",
        "ben": "for",
        "béx": "link",
        "biv": "every",
        "blo": "about",
        "bot": "(?)",
        "brí": "two",
        "can": "always",
        "çan": "can(?)",
        "cav": "live",
        "çev": "thank",
        "çir": "organism",
        "con": "foundation",
        "çúr": "learn",
        "dag": "(?)",
        "daš": "dome towers",
        "don": "like",
        "een": "any",
        "éla": "(?)",
        "emí": "decide(?); win(?)",
        "fam": "far",
        "faš": "near",
        "fel": "row",
        "fuš": "change color(?)",
        "gan": "empire",
        "gaþ": "yet",
        "gel": "write",
        "gid": "excavate",
        "glo": "begin",
        "gor": "time",
        "har": "year",
        "her": "number",
        "hev": "word",
        "hík": "rifle",
        "húr": "find",
        "iné": "more than",
        "íst": "them",
        "ixa": "(?)",
        "kæm": "what",
        "kæt": "only",
        "kag": "original",
        "ken": "I am",
        "klé": "example",
        "klé": "example",
        "kor": "book",
        "kro": "move",
        "læn": "gain(?)",
        "lan": "only",
        "laþ": "highest ones(?)",
        "laþ": "elite(?)",
        "lem": "ink",
        "leš": "rule",
        "lis": "arrive",
        "lon": "discover",
        "lúk": "survey",
        "man": "existence",
        "mer": "watch",
        "mes": "require",
        "met": "this",
        "min": "woman",
        "mís": "speak",
        "mít": "there",
        "mor": "mother(?)",
        "mot": "which",
        "naš": "part",
        "nem": "gather(?)",
        "nía": "new",
        "oko": "black",
        "omd": "(?)",
        "pac": "city",
        "pal": "anyway(?)",
        "pam": "or",
        "pan": "trust",
        "pod": "each",
        "púg": "prove(?)",
        "rak": "class(?)",
        "ram": "good",
        "rek": "class(?)",
        "rem": "flow",
        "ril": "no",
        "riš": "twenty",
        "rís": "eat",
        "ron": "(?)",
        "rov": "person",
        "rúb": "but",
        "rúé": "route",
        "rún": "zero",
        "sek": "have",
        "sel": "Write",
        "šem": "you",
        "sen": "three",
        "set": "us",
        "sev": "age",
        "sex": "have",
        "sín": "get",
        "šin": "able",
        "šol": "prepare",
        "šúþ": "death",
        "tag": "give",
        "tam": "fire",
        "tel": "guild",
        "ten": "simple",
        "ter": "tree",
        "tér": "help",
        "tes": "group",
        "tíg": "work",
        "tor": "four",
        "túl": "grow",
        "umt": "(?)",
        "úrú": "community at large",
        "úša": "formula",
        "vat": "five",
        "váu": "event(?)",
        "vax": "linking",
        "vog": "nature",
        "xæg": "act(?)",
        "xag": "act(?)",
        "xat": "(?)",
        "xlé": "example",
        "yar": "day",
        "yim": "see",
        "zik": "pod",
        "ziþ": "low",
        "þoe": "how",
        "ar": "go(?)",
        "b'": "to ",
        "b’": "to ",
        "ba": "beast",
        "çé": "fault",
        "co": "of",
        "ðo": "how",
        "du": "food",
        "dú": "food",
        "eg": "(?)",
        "el": "high",
        "fa": "one",
        "g’": "and ",
        "go": "(?)",
        "ín": "any",
        "ír": "bandage",
        "l'": "has ",
        "l’": "has ",
        "mo": "that(?)",
        "n'": "around",
        "n’": "around",
        "ne": "around",
        "né": "root",
        "ní": "new",
        "ón": "myself",
        "ox": "of",
        "po": "mouth(?)",
        "pó": "bulb",
        "rú": "that",
        "se": "at",
        "sé": "design",
        "t'": "in ",
        "t’": "in ",
        "ta": "it(?)",
        "te": "with",
        "to": "place",
        "x’": "for",
        "xa": "few",
        "xó": "if(?)",
        "ze": "him/her",
        "zu": "end",
        "zú": "me",
    }
    
    if dniword in dnidict:
        return dnidict[dniword]
    else:
        return dniword


translation = ""

if args.ots:
    phrase = ots2nts(args.phrase.lower())
else:
    phrase = args.phrase.lower()    

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

phrase = phrase.split(' ')
print(">>", phrase, "<<")

negation = 0
kenvoo = 0

for word in phrase:
    if word == " " or word == "":
        continue

    if (word.startswith("re") or word.startswith("r'") or word.startswith("r’")) and word != "re'dæntí" and word != "re’dæntí" and word != "rek" and word != "relyima" and word != "rem" and word != "rema" and word != "remesfet" and word != "remesfeteþ":
        translation = translation + " the"
        word = word[2:]
    elif word.startswith("bre"):
        translation = translation + " to the"
        word = word[3:]
    elif word.startswith("fre"):
        translation = translation + " at the"
        word = word[3:]
    elif word.startswith("g're") or word.startswith("g’re") or word.startswith("gre"):
        translation = translation + " and the"
        word = word[3:]
    elif word.startswith("mre"):
        translation = translation + " from the"
        word = word[3:]
    elif word.startswith("tre"):
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

    if (word.startswith("ga") or word.startswith("g'") or word.startswith("g’")) and word != "garkalec" and word != "garísen" and word != "gartavo" and word != "garano" and word != "garkal" and word != "galon" and word != "galpo" and word != "garoš" and word != "garoþ" and word != "garo" and word != "gan" and word != "gaþ":
        translation = translation + " and"
        word = word[2:]

    if (word.startswith("fe") or word.startswith("f'") or word.startswith("f’")) and word != "fentasenta" and word != "feltan" and word != "ferem" and word != "fena" and word != "fel":
        translation = translation + " on"
        word = word[2:]

    if (word.startswith("me") or word.startswith("m'") or word.startswith("m’")) and word != "megóré" and word != "mepord" and word != "melin" and word != "merk" and word != "meúr" and word != "mer" and word != "mes" and word != "met" and word != "m'la" and word != "m’la":
        translation = translation + " from"
        word = word[2:]
        
    if (word.startswith("te") or word.startswith("t'") or word.startswith("t’")) and word != "teldú'šol" and word != "teldú’šol" and word != "telbacen" and word != "tefúnet" and word != "telbírí" and word != "terelin" and word != "telrov" and word != "tetemo" and word != "telší" and word != "telúk" and word != "teneš" and word != "tema" and word != "temo" and word != "tel" and word != "ten" and word != "ter" and word != "tes":
        translation = translation + " with"
        word = word[2:]

    if word.startswith("xe") or word.startswith("x'") or word.startswith("x’"):
        translation = translation + " for"
        word = word[2:]

    if word.endswith("ox"):
        translation = translation + " of"
        word = word[:-2]
    elif word.startswith("ox"):
        translation = translation + " of"
        word = word[2:]

    if word.endswith("ó") and word != "gestó" and word != "cotó" and word != "ðénó" and word != "pabó" and word != "aró" and word != "pó" and word != "xó":
        translation = translation + " my"
        word = word[:-1]
        if word.endswith("'") or word.endswith("’"):
            word = word[:-1]
    elif word.endswith("om") and word != "trom":
        translation = translation + " your"
        word = word[:-2]
        if word.endswith("'") or word.endswith("’"):
            word = word[:-1]
    elif word.endswith("on") and word != "galon" and word != "muxon" and word != "ziþon" and word != "elon" and word != "con" and word != "don" and word != "lon" and word != "ron":
        translation = translation + " his/her"
        word = word[:-2]
        if word.endswith("'") or word.endswith("’"):
            word = word[:-1]
    elif word.endswith("ot") and word != "gormot" and word != "h'rot" and word != "h’rot" and word != "robot" and word != "tomot" and word != "vamot" and word != "bot" and word != "mot":
        translation = translation + " our"
        word = word[:-2]
        if word.endswith("'") or word.endswith("’"):
            word = word[:-1]
    elif word.endswith("omí"):
        translation = translation + " your"
        word = word[:-3]
        if word.endswith("'") or word.endswith("’"):
            word = word[:-1]
    elif word.endswith("os"):
        translation = translation + " their"
        word = word[:-2]
        if word.endswith("'") or word.endswith("’"):
            word = word[:-1]

        
    if word == "ril":
        negation = 1
        continue
        
    if word == "kenen":
        kenvoo = 1
        continue
    if kenvoo == 1:
        if word == "vúhí":
            translation = translation + " could be"
            kenvoo = 0
            continue
        else:
            translation = translation + " is"
            kenvoo = 0

    if word.startswith("bodol"):
        if negation == 1:
            mood = "will not have been "
            negation = 0
        else:
            mood = "will have been "
        word = word[5:]
        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "ing"
        elif word.endswith("en") and word != "kenen":
            word = word[:-2]
            translation = translation + " (s/he) " + mood + translate(word) + "ing"
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + "ing"
        elif word.endswith("tí") and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "ing"
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + "ing"
        else:
            translation = translation + " I "      + mood + translate(word) + "ing"
        continue
            
    elif word.startswith("bodo"):
        if negation == 1:
            mood = "will not be "
            negation = 0
        else:
            mood = "will be "
        word = word[4:]
        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "ing"
        elif word.endswith("en") and word != "kenen":
            word = word[:-2]
            translation = translation + " (s/he) " + mood + translate(word) + "ing"
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + "ing"
        elif word.endswith("tí") and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "ing"
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + "ing"
        else:
            translation = translation + " I "      + mood + translate(word) + "ing"
        continue

    elif word.startswith("boko"):
        if negation == 1:
            mood = "will not have "
            negation = 0
        else:
            mood = "will have "
        word = word[4:]
        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "en"
        elif word.endswith("en") and word != "kenen":
            word = word[:-2]
            translation = translation + " (s/he) " + mood + translate(word) + "en"
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + "en"
        elif word.endswith("tí") and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "en"
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + "en"
        else:
            translation = translation + " I "      + mood + translate(word) + "en"
        continue
        
    elif word.startswith("bol"):
        if negation == 1:
            mood = "will not have "
            negation = 0
        else:
            mood = "will have "
        word = word[3:]
        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "en"
        elif word.endswith("en") and word != "kenen":
            word = word[:-2]
            translation = translation + " (s/he) " + mood + translate(word) + "en"
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + "en"
        elif word.endswith("tí") and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "en"
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + "en"
        else:
            translation = translation + " I "      + mood + translate(word) + "en"
        continue

    elif word.startswith("bo") and not word.startswith("boken") and word != "bonú" and word != "bonúec" and word != "borta" and word != "bot":
        if negation == 1:
            mood = "will not "
            negation = 0
        else:
            mood = "will "
        word = word[2:]
        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word)
        elif word.endswith("en") and word != "kenen":
            word = word[:-2]
            translation = translation + " (s/he) " + mood + translate(word)
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word)
        elif word.endswith("tí") and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word)
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word)
        elif word != "ken":
            translation = translation + " I "      + mood + translate(word)
        continue

    elif word.startswith("kobol"):
        if negation == 1:
            mood = "would not have "
            negation = 0
        else:
            mood = "would have "
        word = word[5:]
        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "ed"
        elif word.endswith("en") and word != "kenen":
            word = word[:-2]
            translation = translation + " (s/he) " + mood + translate(word) + "ed"
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + "ed"
        elif word.endswith("tí") and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "ed"
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + "ed"
        elif word != "ken":
            translation = translation + " I "      + mood + translate(word) + "ed"
        continue

    elif word.startswith("kodol"):
        if negation == 1:
            mood = "have not been "
            negation = 0
        else:
            mood = "have been "
        word = word[5:]
        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "ing"
        elif word.endswith("en") and word != "kenen":
            word = word[:-2]
            mood = mood.replace("have", "has")
            translation = translation + " (s/he) " + mood + translate(word) + "ing"
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + "ing"
        elif word.endswith("tí") and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "ing"
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + "ing"
        elif word != "ken":
            translation = translation + " I "      + mood + translate(word) + "ing"
        continue

    elif word.startswith("kodo"):
        if negation == 1:
            mood = "were not "
            negation = 0
        else:
            mood = "were "
        word = word[4:]
        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "ing"
        elif word.endswith("en") and word != "kenen":
            word = word[:-2]
            mood = mood.replace("were", "was")
            translation = translation + " (s/he) " + mood + translate(word) + "ing"
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + "ing"
        elif word.endswith("tí") and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "ing"
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + "ing"
        elif word != "ken":
            mood = mood.replace("were", "was")
            translation = translation + " I "      + mood + translate(word) + "ing"
        continue

    elif word.startswith("kol"):
        if negation == 1:
            mood = "had not "
            negation = 0
        else:
            mood = "had "
        word = word[3:]
        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "en"
        elif word.endswith("en") and word != "kenen":
            word = word[:-2]
            translation = translation + " (s/he) " + mood + translate(word) + "en"
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + "en"
        elif word.endswith("tí") and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "en"
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + "en"
        elif word != "ken":
            translation = translation + " I "      + mood + translate(word) + "en"
        continue

    elif word.startswith("ko") and not word.startswith("koken") and word != "kor'nía" and word != "kor’nía" and word != "kor'vax" and word != "kor’vax" and word != "korman" and word != "korvax" and word != "korfa" and word != "koca" and word != "kota" and word != "kor":
        word = word[2:]
        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            if negation == 1:
                translation = translation + " you didn't "    + translate(word)
                negation = 0
            else:
                translation = translation + " you "           + translate(word) + "ed"
        elif word.endswith("en") and word != "kenen":
            word = word[:-2]
            if negation == 1:
                translation = translation + " (s/he) didn't " + translate(word)
                negation = 0
            else:
                translation = translation + " (s/he) "        + translate(word) + "ed"
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            if negation == 1:
                translation = translation + " we didn't "     + translate(word)
                negation = 0
            else:
                translation = translation + " we "            + translate(word) + "ed"
        elif word.endswith("tí") and word != "kentí":
            word = word[:-2]
            if negation == 1:
                translation = translation + " you didn't "    + translate(word)
                negation = 0
            else:
                translation = translation + " you "           + translate(word) + "ed"
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            if negation == 1:
                translation = translation + " (they) didn't " + translate(word)
                negation = 0
            else:
                translation = translation + " (they) "        + translate(word) + "ed"
        elif word != "ken":
            word = word[:-2]
            if negation == 1:
                translation = translation + " I didn't "      + translate(word)
                negation = 0
            else:
                translation = translation + " I "             + translate(word) + "ed"
        continue

    elif (word.startswith("le") or word.startswith("l'") or word.startswith("l’")) and word != "lem" and word != "lena" and word != "lenita" and word != "lesa" and word != "leš":
        if negation == 1:
            mood = "have not "
            negation = 0
        else:
            mood = "have "
        word = word[2:]
        if word.endswith("em") and word != "kenem":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "en"
        elif word.endswith("en") and word != "kenen":
            word = word[:-2]
            mood = mood.replace("have", "has")
            translation = translation + " (s/he) " + mood + translate(word) + "en"
        elif word.endswith("et") and word != "kenet":
            word = word[:-2]
            translation = translation + " we "     + mood + translate(word) + "en"
        elif word.endswith("tí") and word != "kentí":
            word = word[:-2]
            translation = translation + " you "    + mood + translate(word) + "en"
        elif word.endswith("ít") and word != "kenít":
            word = word[:-2]
            translation = translation + " (they) " + mood + translate(word) + "en"
        elif word != "ken":
            translation = translation + " I "      + mood + translate(word) + "en"
        continue

    if word.endswith("em") and not word.endswith("kenem"):
        word = word[:-2]
        translation = translation + " " + translate(word)
        continue
    elif word.endswith("en") and not word.endswith("kenen") and not word.endswith("ken"):
        word = word[:-2]
        if translation.endswith("can"):
            translation = translation + " " + translate(word)
        else:
            translation = translation + " " + translate(word) + "s"
        continue
    elif word.endswith("et") and not word.endswith("kenet"):
        word = word[:-2]
        translation = translation + " " + translate(word)
        continue
    elif word.endswith("tí") and not word.endswith("kentí"):
        if word == "cotótí" or word == "šemtí":
            translation = translation + " " + translate(word)
            continue
        else:
            word = word[:-2]
            translation = translation + " " + translate(word) + "s"
            continue
    elif word.endswith("ít") and not word.endswith("kenít"):
        word = word[:-2]
        translation = translation + " " + translate(word)
        continue


    if negation == 1:
        translation = translation + " no(t) "
    else:
        translation = translation + " " + translate(word)
    
    
#    engword = engword.replace("do-", "is ")
#    engword = engword.replace("dol-", "has been ")
#    engword = engword.replace("-ij", "ed")

#    engword = engword.replace("-tí", "s")

#    engword = engword.replace("-al", "ing")
#    engword = engword.replace("-aloþ", "er")
#    engword = engword.replace("-in", "ed")

#    engword = engword.replace("-am", "member(?)")
#    engword = engword.replace("-ec", "y")
#    engword = engword.replace("-et", "ful")
#    engword = engword.replace("-eþ", "Noun-forming suffix")
#    engword = engword.replace("-eš", "ly")
#    engword = engword.replace("-t", "y")

#    engword = engword.replace("-tan", "er")
#    engword = engword.replace("-tav", "tion")

#    engword = engword.replace("-þ", "ty")
#    engword = engword.replace("-š", "ly")

#    engword = engword.replace("d'", "again-")
#    engword = engword.replace("de-", "again")
#    engword = engword.replace("d’", "again-")

#    
#    engword = engword.replace("-sí", " times 25")
#    engword = engword.replace("-ra", " times 25^2")
#    engword = engword.replace("-lan", " times 25^3")
#    engword = engword.replace("-len", " times 25^3")
#    engword = engword.replace("-mel", " times 25^4")
#    engword = engword.replace("-blo", " times 25^5")
    
    
        

print(translation)
