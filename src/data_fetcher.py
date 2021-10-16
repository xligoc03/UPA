import json
import re
from os.path import exists, join
from os import makedirs
import xml.etree.ElementTree as ET
from typing import Dict, List

import requests
import pandas as pd

from src.config import BASE_DATA_FOLDER, REGION_CODES, DATA_URL, SCHOOLS_DATA_URL


def fetch_schools() -> Dict:
    if not exists(join(BASE_DATA_FOLDER, "xml")):
        makedirs(join(BASE_DATA_FOLDER, "xml"))

    school_data_file_path = join(BASE_DATA_FOLDER, "xml/schools.xml")

    # check if file exists
    if not exists(school_data_file_path):
        # download file first, save, than open
        request_data = requests.get(SCHOOLS_DATA_URL)
        with open(school_data_file_path, 'wb') as file:
            file.write(request_data.content)

    root = ET.parse(school_data_file_path, ).getroot()

    all_items = []
    for root_elem in root.findall('PravniSubjekt'):
        item_dict = {}
        for elem in root_elem.findall('./Reditelstvi'):
            name = elem.find('./RedPlnyNazev').text

            address_item = parse_address(elem, ['RedAdresa1', 'RedAdresa2', 'RedAdresa3'])
            address_item['okres_kod'] = elem.find('./Okres').text

            school_items = []

            for director_elem in elem.findall('Reditel'):
                director_item = {
                    'meno': director_elem.find('./ReditelJmeno').text.split(' ')[0]
                        if director_elem.find('./ReditelJmeno') is not None else None,
                    'priezvisko': director_elem.find('./ReditelJmeno').text.split(' ')[1]
                        if director_elem.find('./ReditelJmeno') is not None else None,
                    'adresa': parse_address(director_elem, ['ReditelAdresa1', 'ReditelAdresa2', 'ReditelAdresa3'])
               }

            for schools_elem in root_elem.findall('./SkolyZarizeni'):
                for school_elem in schools_elem.findall('./SkolaZarizeni'):
                    school_items.append({
                        'nazov': school_elem.find('SkolaPlnyNazev').text,
                        'typ': school_elem.find('SkolaDruhTyp').text,
                        'kapacita': school_elem.find('SkolaKapacita').text
                    })

                item_dict['nazov'] = name
                item_dict['adresa'] = address_item
                item_dict['riaditel'] = director_item
                item_dict['zariadenia'] = school_items

            all_items.append(item_dict)

    return all_items


def parse_address(element: ET.Element, tag_names: List) -> Dict:
    common_tags = sorted(list(set(list(map(lambda x: x.tag, element.findall('./')))) & set(tag_names)), reverse=True)

    if len(common_tags) == 0:
        return None

    postal_code = None
    city = None

    address = element.find(f"./{common_tags[2]}").text
    city_district = element.find(f"./{common_tags[1]}").text
    if element.find(f"./{common_tags[0]}") is not None and element.find(f"./{common_tags[0]}").text is not None:
        postal_code = re.search('([0-9 ])*', element.find(f"./{common_tags[0]}").text).group(0).replace(" ", "")
        city = re.search(' \D+[ 0-9]*', element.find(f"./{common_tags[0]}").text).group(0).strip()

    return {'ulica': address, 'mesto': city, 'mestska_cast': city_district, 'psc': postal_code}


def clean_school_data():
    schools = fetch_schools()
    tmp = json.dumps(schools, ensure_ascii=False)
    return tmp


def fetch_regions() -> pd.DataFrame:
    if not exists(join(BASE_DATA_FOLDER, "csv")):
        makedirs(join(BASE_DATA_FOLDER, "csv"))

    regions_data_file_path = join(BASE_DATA_FOLDER, "csv/regions.csv")
    # check if file exists
    if exists(regions_data_file_path):
        # open file in pandas dataframe
        return pd.read_csv(regions_data_file_path)

    # dowload file first, save, than open
    request_data = requests.get(DATA_URL)
    with open(regions_data_file_path, 'wb') as file:
        file.write(request_data.content)

    return pd.read_csv(regions_data_file_path)


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
