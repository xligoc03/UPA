"""
Project configuration and static values for fetcher and database client
"""

import os

# data urls
SCHOOLS_DATA_URL = "https://rejstriky.msmt.cz/opendata/vrejcelk.xml"
DATA_URL = "https://www.czso.cz/documents/62353418/143522504/130142-21data043021.csv/760fab9c-d079-4d3a-afed-59cbb639e37d?version=1.1"

# root folder
ROOT_PATH = os.path.dirname(os.path.realpath(__file__)).rstrip("src")

# xml data folder
BASE_DATA_FOLDER = ROOT_PATH + "data"

# DB
DB_PORT = "27017"
DB_USER = "root"
DB_PSWD = "password"
DB_HOST = "localhost"

# connection string
MONGO_CONNECTION_STRING = f"mongodb://{DB_USER}:{DB_PSWD}@{DB_HOST}:{DB_PORT}"

MONGO_SCHOOLS_DB_NAME = "schools"
MONGO_SCHOOLS_COLLECTION_NAME = "all_schools"
MONGO_POPULATION_COLLECTION_NAME = "population"

# regions codes whole republic included
REGION_CODES = {19, 3018, 3026, 3034, 3042, 3051, 3069, 3077, 3085, 3093, 3107, 3115, 3123, 3131,
                3140}

OKRES_IN_REGIONS = {
    3018: [
        "CZ0110"
        ], # Hl.m. Praha
    3026: [
        "CZ0211", "CZ0212", "CZ0213", "CZ0214", "CZ0215", "CZ0216", "CZ0217", "CZ0218", "CZ0219", "CZ021A", "CZ021B", "CZ021C"
        ], # Středočeský kraj
    3034: [
        "CZ0311", "CZ0312", "CZ0313", "CZ0314", "CZ0315", "CZ0316", "CZ0317"
        ], # Jihočeský kraj
    3042: [
        "CZ0321",
        "CZ0322",
        "CZ0323",
        "CZ0324",
        "CZ0325",
        "CZ0326",
        "CZ0327"
        ], # Plzeňský kraj
    3051: [
        "CZ0411",
        "CZ0412",
        "CZ0413"
    ], # Karlovarský kraj
    3069: [
        "CZ0421",
        "CZ0422",
        "CZ0423",
        "CZ0424",
        "CZ0425",
        "CZ0426",
        "CZ0427"
    ], # Ústecký kraj
    3077: [
        "CZ0511",
        "CZ0512",
        "CZ0513",
        "CZ0514"
    ], # Liberecký kraj
    3085: [
        "CZ0521",
        "CZ0522",
        "CZ0523",
        "CZ0524",
        "CZ0525"
    ], # Královéhradecký kraj
    3093: [
        "CZ0531",
        "CZ0532",
        "CZ0533",
        "CZ0534"
    ], # Pardubický kraj
    3107: [
        "CZ0611",
        "CZ0612",
        "CZ0613",
        "CZ0614",
        "CZ0615"
    ], # Kraj Vysočina
    3115: [
        "CZ0621",
        "CZ0622",
        "CZ0623",
        "CZ0624",
        "CZ0625",
        "CZ0626",
        "CZ0627"
    ], # Jihomoravský kraj
    3123: [
        "CZ0711",
        "CZ0712",
        "CZ0713",
        "CZ0714",
        "CZ0715"
    ], # Olomoucký kraj
    3131: [
        "CZ0721",
        "CZ0722",
        "CZ0723",
        "CZ0724"
        ], # Zlínský kraj
    3140: [
        "CZ0811",
        "CZ0812",
        "CZ0813",
        "CZ0814",
        "CZ0815",
        "CZ0816"
    ]  # Moravskoslezský kraj
}

OKRES_CODES = {
    40169: "CZ0211",
    40177: "CZ0212",
    40185: "CZ0213",
    40193: "CZ0214",
    40207: "CZ0215",
    40215: "CZ0216",
    40223: "CZ0217",
    40231: "CZ0218",
    40240: "CZ0219",
    40258: "CZ021A",
    40266: "CZ021B",
    40274: "CZ021C",
    40282: "CZ0311",
    40291: "CZ0312",
    40304: "CZ0313",
    40312: "CZ0314",
    40321: "CZ0315",
    40339: "CZ0316",
    40347: "CZ0317",
    40355: "CZ0321",
    40363: "CZ0322",
    40371: "CZ0323",
    40380: "CZ0324",
    40398: "CZ0325",
    40401: "CZ0326",
    40410: "CZ0327",
    40428: "CZ0411",
    40436: "CZ0412",
    40444: "CZ0413",
    40452: "CZ0421",
    40461: "CZ0422",
    40479: "CZ0423",
    40487: "CZ0424",
    40495: "CZ0425",
    40509: "CZ0426",
    40517: "CZ0427",
    40525: "CZ0511",
    40533: "CZ0512",
    40541: "CZ0513",
    40550: "CZ0514",
    40568: "CZ0521",
    40576: "CZ0522",
    40584: "CZ0523",
    40592: "CZ0524",
    40606: "CZ0525",
    40614: "CZ0531",
    40622: "CZ0532",
    40631: "CZ0533",
    40649: "CZ0534",
    40657: "CZ0611",
    40665: "CZ0612",
    40673: "CZ0613",
    40681: "CZ0614",
    40690: "CZ0615",
    40703: "CZ0621",
    40711: "CZ0622",
    40720: "CZ0623",
    40738: "CZ0624",
    40746: "CZ0625",
    40754: "CZ0626",
    40762: "CZ0627",
    40771: "CZ0711",
    40789: "CZ0712",
    40797: "CZ0713",
    40801: "CZ0714",
    40819: "CZ0715",
    40827: "CZ0721",
    40835: "CZ0722",
    40843: "CZ0723",
    40851: "CZ0724",
    40860: "CZ0811",
    40878: "CZ0812",
    40886: "CZ0813",
    40894: "CZ0814",
    40908: "CZ0815",
    40916: "CZ0816"
}

# school types codes
# materske skoly
MS = {"A00", "A10", "A13", "A14", "A15", "A16"}
# zakladne skoly
ZS = {"B00", "B10", "B13", "B14", "B16", "B31"}
# stredne skoly
SS = {"C00", "C10", "C16", "C93", "B16", "B31"}
# umelecke a jazykove skoly
US_JS = {"F10", "F20", "F29", "D00", "D10", "D16"}
# jedalne
CANTEENS = {"L11", "L12", "L13", "L15", "L19"}
# kluby a druziny
SCHOOL_CLUB = {"G21", "G22"}
