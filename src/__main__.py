#!/usr/bin/python3
"""
Dockerized application for fetching and processing data about educational system in Czech Republic
"""
import os.path
import sys
from database.mongo_init import MongoDatabase
from config import BASE_DATA_FOLDER


# pylint: disable=missing-function-docstring
def main() -> int:
    mongo_db = MongoDatabase(27017)

    db_client = mongo_db.mongo_client
    mongo_db.print_info()
    mongo_db.import_xml_data(os.path.join(BASE_DATA_FOLDER, "xml/vrejcelk.xml"), "schools", "all")
    for doc in db_client["schools"]["all"].find({}).limit(10):
        print(doc, "\n")

    return mongo_db.check_connection(db_client)


if __name__ == '__main__':
    sys.exit(main())
