import os
import records
import logme

from .env import DATABASE_URL, SQL_PATH, SQL_SCHEMA_PATH


@logme.log
class Database:
    def __init__(self, db_url: str=None):
        self.db_url = db_url or DATABASE_URL
        self.db = records.Database(db_url=self.db_url)

    @property
    def schemas(self):
        # Get the schemas.
        for root, _, files in os.walk(SQL_SCHEMA_PATH):
            for _file in files:
                yield f"{root}/{_file}"

    def initialize(self):
        for schema in sorted(self.schemas):
            self.db.query_file(schema)
            # TODO: assert was successful.
            # TODO: add logging.



# db = Database(db_url=DATABASE_URL)
