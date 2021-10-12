#!/usr/bin/python3
"""
Dockerized application for fetching and processing data about educational system in Czech Republic
"""
import sys
from database.mongo_init import MongoDatabase


# pylint: disable=missing-function-docstring
def main() -> int:
    mongo_db = MongoDatabase(27017)
    mongo_db.print_info()

    #db_client = mongo_db.create_client()

    return mongo_db.check_connection()


if __name__ == '__main__':
    sys.exit(main())
