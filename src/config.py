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

# regions codes
REGION_CODES = {3018, 3026, 3034, 3042, 3051, 3069, 3077, 3085, 3093, 3107, 3115, 3123, 3131, 3140}

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
