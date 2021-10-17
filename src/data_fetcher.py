"""
Input data fetcher for fetching and cleaning data
"""

import json
import re
from os.path import exists, join
from os import makedirs
import xml.etree.ElementTree as ET
from typing import Dict, List

import requests
import pandas as pd

from src.config import BASE_DATA_FOLDER, REGION_CODES, DATA_URL, SCHOOLS_DATA_URL


def fetch_schools() -> str:
    if not exists(join(BASE_DATA_FOLDER, "xml")):
        makedirs(join(BASE_DATA_FOLDER, "xml"))

    school_data_file_path = join(BASE_DATA_FOLDER, "xml/schools.xml")

    # check if file exists
    if not exists(school_data_file_path):
        # download file first, save, than open
        request_data = requests.get(SCHOOLS_DATA_URL)
        with open(school_data_file_path, 'wb') as file:
            file.write(request_data.content)

    return school_data_file_path


def parse_address(element: ET.Element, tag_names: List) -> Dict:
    """
    Parse address from xml elements
    :param element: root element
    :param tag_names: element names
    :return: dictionary containing street, city, city district and postal code
    """
    common_tags = sorted(list(set(list(map(lambda x: x.tag, element.findall('./')))) & set(tag_names)), reverse=True)

    if len(common_tags) == 0:
        return None

    postal_code = None
    city = None

    street = element.find(f"./{common_tags[2]}").text
    city_district = element.find(f"./{common_tags[1]}").text
    if element.find(f"./{common_tags[0]}") is not None and element.find(f"./{common_tags[0]}").text is not None:
        postal_code = re.search(r'([0-9 ])*', element.find(f"./{common_tags[0]}").text).group(0).replace(" ", "")
        city = re.search(r' \D+[ 0-9]*', element.find(f"./{common_tags[0]}").text).group(0).strip()

    return {'ulica': street, 'mesto': city, 'mestska_cast': city_district, 'psc': postal_code}


def clean_school_data() -> str:
    """
    Clean data about schools and save to JSON string with dict format.

    :note: information about XML file structure can be found on :url: https://rejstriky.msmt.cz/opendata/metadata/PopisVetyVrejskol.txt

    :return: string in JSON format containing information about schools
    """
    schools_data_xml_file = fetch_schools()

    with open(schools_data_xml_file) as file:
        root = ET.parse(file, ).getroot()

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

    return json.dumps(all_items, ensure_ascii=False)


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
