import records

from .env import DATABASE_URL, SQL_PATH, SQL_SCHEMA_PATH


class Database:
    def __init__(db_url):
        self.db_url = db_url
        self.db = records.Database(db_url=DATABASE_URL)

    def initialize(self):

        # Get the schemas.
        schemas = []
        for root, dirs, files in os.walk("."):
            for _file in files:
                schemas.append(f"{root}{_file}):

        for schema in sorted(schemas):
            self.db.query_file(schema)
            # TODO: assert was successful.
            # TODO: add logging.


db = Database(db_url=DATABASE_URL)
