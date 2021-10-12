#!/usr/bin/python3
"""
Dockerized application for fetching and processing data about educational system in Czech Republic
"""
import sys
from database.mongo_init import MongoDatabase


# pylint: disable=missing-function-docstring
def main() -> int:
    mongo_db = MongoDatabase(27017)

    db_client = mongo_db.create_client()
    mongo_db.print_info()

    return mongo_db.check_connection(db_client)


if __name__ == '__main__':
    sys.exit(main())
