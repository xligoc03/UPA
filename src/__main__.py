#!/usr/bin/python3
"""
Dockerized application for fetching and processing data about educational system in Czech Republic
"""
import os
import sys
from database.mongo_database import MongoDatabase
from src.data_fetcher import DataFetcher


# pylint: disable=missing-function-docstring
def main() -> int:
    mongo_db = MongoDatabase(27017)
    get_data = DataFetcher()

    db_client = mongo_db.mongo_client

    # DROP TABLE to be sure we work in clean environment
    db_client.drop_database("schools")
    # create DB
    database = mongo_db.create_db("schools")
    # switch collection to schools
    collection = database["all_schools"]
    # import data for schools
    mongo_db.import_data(get_data.schools, collection)
    # switch collection to cz population
    collection = database["population"]
    # import data for population
    mongo_db.import_data(get_data.regions, collection)

    return os.EX_OK


if __name__ == '__main__':
    sys.exit(main())
