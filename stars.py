import random

NAMED_STARS = [
    "Acamar",
    "Achernar",
    "Achird",
    "Acrab",
    "Acrux",
    "Acubens",
    "Adhafera",
    "Adhara",
    "Adhil",
    "Ain",
    "Ainalrami",
    "Aladfar",
    "Alamak",
    "Alathfar",
    "Albaldah",
    "Albali",
    "Albireo",
    "Alchiba",
    "Alcor",
    "Alcyone",
    "Aldebaran",
    "Alderamin",
    "Aldhanab",
    "Aldhibah",
    "Aldulfin",
    "Alfirk",
    "Algedi",
    "Algenib",
    "Algieba",
    "Algol",
    "Algorab",
    "Alhena",
    "Alioth",
    "Aljanah",
    "Alkaid",
    "Al Kalb al Rai",
    "Alkalurops",
    "Alkaphrah",
    "Alkarab",
    "Alkes",
    "Almaaz",
    "Almach",
    "Al Minliar al Asad",
    "Alnair",
    "Alnasl",
    "Alnilam",
    "Alnitak",
    "Alniyat",
    "Alphard",
    "Alphecca",
    "Alpheratz",
    "Alpherg",
    "Alrakis",
    "Alrescha",
    "Alruba",
    "Alsafi",
    "Alsciaukat",
    "Alsephina",
    "Alshain",
    "Alshat",
    "Altair",
    "Altais",
    "Alterf",
    "Aludra",
    "Alula Australis",
    "Alula Borealis",
    "Alya",
    "Alzirr",
    "Ancha",
    "Angetenar",
    "Ankaa",
    "Anser",
    "Antares",
    "Arcturus",
    "Arkab Posterior",
    "Arkab Prior",
    "Arneb",
    "Ascella",
    "Asellus Australis",
    "Asellus Borealis",
    "Ashlesha",
    "Asellus Primus",
    "Asellus Secundus",
    "Asellus Thertius",
    "Asmidiske",
    "Aspidiske",
    "Asterope",
    "Athebyne",
    "Atik",
    "Atlas",
    "Atria",
    "Avior",
    "Azelfafage",
    "Azha",
    "Azmidi",
    "Barnard's Star",
    "Baten Kaitos",
    "Beemim",
    "Beid",
    "Bellatrix",
    "Betelgeuse",
    "Bharani",
    "Biham",
    "Botein",
    "Brachium",
    "Bunda",
    "Canopus",
    "Capella",
    "Caph",
    "Castor",
    "Castula",
    "Cebalrai",
    "Celaeno",
    "Cervantes",
    "Chalawan",
    "Chamukuy",
    "Chara",
    "Chertan",
    "Copernicus",
    "Cor Caroli",
    "Cujam",
    "Cursa",
    "Dabih",
    "Dalim",
    "Deneb",
    "Deneb Algedi",
    "Denebola",
    "Diadem",
    "Diphda",
    "Dschubba",
    "Dubhe",
    "Dziban",
    "Edasich",
    "Electra",
    "Elgafar",
    "Elkurud",
    "Elnath",
    "Eltanin",
    "Enif",
    "Errai",
    "Fafnir",
    "Fang",
    "Fawaris",
    "Felis",
    "Fomalhaut",
    "Fulu",
    "Fumalsamakah",
    "Furud",
    "Fuyue",
    "Gacrux",
    "Garnet Star",
    "Giausar",
    "Gienah",
    "Ginan",
    "Gomeisa",
    "Graffias",
    "Grumium",
    "Hadar",
    "Haedus",
    "Hamal",
    "Hassaleh",
    "Hatysa",
    "Helvetios",
    "Heze",
    "Homam",
    "Iklil",
    "Intercrus",
    "Izar",
    "Jabbah",
    "Jishui",
    "Kaffaljidhma",
    "Kang",
    "Kaus Australis",
    "Kaus Borealis",
    "Kaus Media",
    "Keid",
    "Khambalia",
    "Kitalpha",
    "Kochab",
    "Kornephoros",
    "Kraz",
    "Kuma",
    "Kurhah",
    "La Superba",
    "Larawag",
    "Lesath",
    "Libertas",
    "Lich",
    "Lilii Borea",
    "Maasym",
    "Mahasim",
    "Maia",
    "Marfark",
    "Marfik",
    "Markab",
    "Markeb",
    "Marsic",
    "Matar",
    "Mebsuta",
    "Megrez",
    "Meissa",
    "Mekbuda",
    "Meleph",
    "Menkalinan",
    "Menkar",
    "Menkent",
    "Menkib",
    "Merak",
    "Merga",
    "Meridiana",
    "Merope",
    "Mesarthim",
    "Miaplacidus",
    "Mimosa",
    "Minchir",
    "Minelauva",
    "Mintaka",
    "Mira",
    "Mirach",
    "Miram",
    "Mirfak",
    "Mirzam",
    "Misam",
    "Mizar",
    "Mothallah",
    "Muliphein",
    "Muphrid",
    "Muscida",
    "Musica",
    "Nahn",
    "Naos",
    "Nashira",
    "Navi",
    "Nekkar",
    "Nembus",
    "Nihal",
    "Nunki",
    "Nusakan",
    "Ogma",
    "Okab",
    "Peacock",
    "Phact",
    "Phecda",
    "Pherkad",
    "Piautos",
    "Pipirima",
    "Pleione",
    "Polaris",
    "Polaris Australis",
    "Polis",
    "Pollux",
    "Porrima",
    "Praecipua",
    "Prima Hyadum",
    "Procyon",
    "Propus",
    "Proxima Centauri",
    "Ran",
    "Rana",
    "Rasalas",
    "Rasalgethi",
    "Rasalhague",
    "Rastaban",
    "Regor",
    "Regulus",
    "Revati",
    "Rigel",
    "Rigil Kentaurus",
    "Rotanev",
    "Ruchbah",
    "Rukbat",
    "Sabik",
    "Saclateni",
    "Sadachbia",
    "Sadalbari",
    "Sadalmelik",
    "Sadalsuud",
    "Sadr",
    "Saiph",
    "Salm",
    "Sargas",
    "Sarin",
    "Sarir",
    "Sceptrum",
    "Scheat",
    "Schedar",
    "Secunda Hyadum",
    "Segin",
    "Seginus",
    "Sham",
    "Shaula",
    "Sheliak",
    "Sheratan",
    "Sirius",
    "Situla",
    "Skat",
    "Spica",
    "Sualocin",
    "Subra",
    "Suhail",
    "Sulafat",
    "Syrma",
    "Tabit",
    "Taiyangshou",
    "Taiyi",
    "Talitha",
    "Tania Australis",
    "Tania Borealis",
    "Tarazed",
    "Tarf",
    "Taygeta",
    "Tegmine",
    "Tejat",
    "Terebellum",
    "Thabit",
    "Theemin",
    "Thuban",
    "Tiaki",
    "Tianguan",
    "Tianyi",
    "Titawin",
    "Tonatiuh",
    "Torcular",
    "Tureis",
    "Ukdah",
    "Unukalhai",
    "Unurgunite",
    "Vega",
    "Veritate",
    "Vindemiatrix",
    "Wasat",
    "Wazn",
    "Wezen",
    "Wurren",
    "Xamidimura",
    "Xuange",
    "Yed Posterior",
    "Yed Prior",
    "Yildun",
    "Zaniah",
    "Zaurak",
    "Zavijava",
    "Zhang",
    "Zibal",
    "Zosma",
    "Zubenelgenubi",
    "Zubenelhakrabi",
    "Zubeneschamali",
    "Pi Persei",
    "Beta Magellan",
    "Beta Renner",
    "Dragon's Egg",
    "Rao",
    "LV-426",
    "Perdide",
    "Delta Pavonis",
    "Omicron Persei",
    "FI Virginis",
    "V1216 Sagittarii",
    "HH Andromedae",
    "Gliese 876",
    "Tau Ceti",
    "Alpha Centauri",
    "Wolf 359 ",
]


GREEK_LETTERS = [
    "Alpha",
    "Beta",
    "Chi",
    "Delta",
    "Epsilon",
    "Eta",
    "Gamma",
    "Iota",
    "Kappa",
    "Lambda",
    "Mu",
    "Nu",
    "Omega",
    "Omicron",
    "Phi",
    "Pi",
    "Psi",
    "Rho",
    "Sigma",
    "Tau",
    "Theta",
    "Upsilon",
    "Xi",
    "Zeta",
]
CONSTELLATIONS = [
    "Andromedae",
    "Aquarii",
    "Aquilae",
    "Arae",
    "Arietis",
    "Aurigae",
    "Bootis",
    "Cancri",
    "Canis",
    "Canum",
    "Capricorni",
    "Carinae",
    "Cassiopeiae",
    "Centauri",
    "Cephei",
    "Ceti",
    "Columbae",
    "Comae",
    "Coronae",
    "Corvi",
    "Crateris",
    "Crucis",
    "Cygni",
    "Delphini",
    "Draconis",
    "Equulei",
    "Eridani",
    "Fornacis",
    "Geminorum",
    "Gruis",
    "Herculis",
    "Hydrae",
    "Leonis",
    "Leporis",
    "Librae",
    "Lyncis",
    "Lyrae",
    "Octantis",
    "Ophiuchi",
    "Orionis",
    "Pavonis",
    "Pegasi",
    "Persei",
    "Phoenicis",
    "Piscis",
    "Piscium",
    "Puppis",
    "Sagittae",
    "Sagittarii",
    "Scorpii",
    "Serpentis",
    "Tauri",
    "Trianguli",
    "Ursae",
    "Velorum",
    "Virginis",
    "Vulpeculae",
]


def random_new_star():
    return " ".join([random.choice(GREEK_LETTERS), random.choice(CONSTELLATIONS)])


def random_new_stars(n: int):
    """return a shuffled list of `n` unique random star names."""
    names = [random_new_star() for _ in range(n + 10)]
    names = list(set(names))
    return random.sample(names, n)


def random_star_names(n_total: int, min_random=0):
    n_named = min(n_total - min_random, len(NAMED_STARS))
    n_random = n_total - n_named
    names = random.sample(NAMED_STARS, n_named) + random_new_stars(n_random)
    random.shuffle(names)
    return names
