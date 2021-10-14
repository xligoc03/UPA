#!/usr/bin/python3
"""
Dockerized application for fetching and processing data about educational system in Czech Republic
"""
import os.path
import sys
from database.mongo_database import MongoDatabase
from config import BASE_DATA_FOLDER
from src.data_fetcher import DataFetcher


# pylint: disable=missing-function-docstring
def main() -> int:
    mongo_db = MongoDatabase(27017)
    get_data = DataFetcher()

    db_client = mongo_db.mongo_client
    mongo_db.print_info()

    # DROP TABLE to be sure we work in clean environment
    db_client.drop_database('schools')
    # import data # TODO vytvorit db a v nej kolekcie pre school a regions data
    # TODO upravit import aby importoval z objektov a nie zo suboru
    mongo_db.import_data(os.path.join(BASE_DATA_FOLDER, "xml/schools.xml"), "schools", "all")

    ########### TEST ###########
    # for doc in db_client["schools"]["all"].find({}).limit(10):
    #     print(doc, "\n")
    ########### TEST ###########

    return mongo_db.check_connection(db_client)


if __name__ == '__main__':
    sys.exit(main())
