from os.path import exists, join
from os import makedirs

import requests
import pandas

from src.config import BASE_DATA_FOLDER, REGION_CODES


def fetch_schools() -> pandas.DataFrame:
    if not exists(join(BASE_DATA_FOLDER, "xml")):
        makedirs(join(BASE_DATA_FOLDER, "xml"))

    school_data_file_path = join(BASE_DATA_FOLDER, "xml/schools.xml")
    # check if file exists
    if exists(school_data_file_path):
        # open file in pandas dataframe
        return pandas.read_xml(school_data_file_path)

    # dowload file first, save, than open
    request_data = requests.get("https://rejstriky.msmt.cz/opendata/vrejcelk.xml")
    with open(school_data_file_path, 'wb') as file:
        file.write(request_data.content)

    return pandas.read_xml(school_data_file_path)


def clean_school_data():
    schools = fetch_schools()
    return schools  # TODO upravit data a vratit ako objekt pripraveny pre import do DB


def fetch_regions() -> pandas.DataFrame:
    if not exists(join(BASE_DATA_FOLDER, "csv")):
        makedirs(join(BASE_DATA_FOLDER, "csv"))

    regions_data_file_path = join(BASE_DATA_FOLDER, "csv/regions.csv")
    # check if file exists
    if exists(regions_data_file_path):
        # open file in pandas dataframe
        return pandas.read_csv(regions_data_file_path)

    # dowload file first, save, than open
    request_data = requests.get("https://www.czso.cz/documents/62353418/143522504/130142"
                                "-21data043021.csv/760fab9c-d079-4d3a-afed-59cbb639e37d"
                                "?version=1.1")
    with open(regions_data_file_path, 'wb') as file:
        file.write(request_data.content)

    return pandas.read_csv(regions_data_file_path)


def clean_regions_data():
    regions_df = fetch_regions()
    regions_df = regions_df.loc[(regions_df['casref_do'] == "2020-12-31") &
                                (regions_df['vuzemi_kod'].isin(REGION_CODES)) &
                                (regions_df['pohlavi_cis'].isnull()) &
                                (regions_df['vek_cis'].isnull())]
    regions_df.drop(
        ["stapro_kod", "pohlavi_cis", "pohlavi_kod", "pohlavi_txt", "vek_cis", "vek_kod",
         "vek_txt", "vuzemi_cis"],
        inplace=True, axis=1)
    return regions_df.to_dict("records")


class DataFetcher:
    def __init__(self):
        self.schools = clean_school_data()
        self.regions = clean_regions_data()
