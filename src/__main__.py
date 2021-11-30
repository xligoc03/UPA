#!/usr/bin/python3
"""
Dockerized application for fetching and processing data about educational system in Czech Republic
"""
import sys
from database.mongo_database import MongoDatabase
from src.data_fetcher import DataFetcher
from config import MONGO_SCHOOLS_DB_NAME, MONGO_SCHOOLS_COLLECTION_NAME, MONGO_POPULATION_COLLECTION_NAME

# pylint: disable=missing-function-docstring
def main() -> int:
    return fetch_and_store_data()


def check_db(db_client, mongo_db):
    """
    Check if database exists or create one
    :param db_client: database client
    :param mongo_db: database class instance
    :return: database
    """
    existing_dbs = db_client.list_database_names()
    if MONGO_SCHOOLS_DB_NAME in existing_dbs:
        return db_client.get_database(MONGO_SCHOOLS_DB_NAME)
    else:
        # create DB
        database = mongo_db.create_db(MONGO_SCHOOLS_DB_NAME)

    return database


def fetch_and_store_data() -> int :
    mongo_db = MongoDatabase(27017)
    get_data = DataFetcher()

    db_client = mongo_db.mongo_client
    database = check_db(db_client, mongo_db)
    res = 0

    existing_collections = db_client[MONGO_SCHOOLS_DB_NAME].list_collection_names()
    if MONGO_POPULATION_COLLECTION_NAME in existing_collections:
        # update data
        res = mongo_db.update_data(get_data.regions, database[MONGO_POPULATION_COLLECTION_NAME])
    else:
        # switch collection to schools
        collection = database[MONGO_SCHOOLS_COLLECTION_NAME]
        # import data for schools
        res = mongo_db.import_data(get_data.schools, collection)
        # switch collection to cz population
        collection = database[MONGO_POPULATION_COLLECTION_NAME]
        # import data for population
        res = mongo_db.import_data(get_data.regions, collection)

    return res


def check_db(db_client, mongo_db):
    """
    Check if database exists or create one
    :param db_client: database client
    :param mongo_db: database class instance
    :return: database
    """
    existing_dbs = db_client.list_database_names()
    if MONGO_SCHOOLS_DB_NAME in existing_dbs:
        return db_client.get_database(MONGO_SCHOOLS_DB_NAME)
    else:
        # create DB
        database = mongo_db.create_db(MONGO_SCHOOLS_DB_NAME)

    return database

if __name__ == '__main__':
    sys.exit(main())
