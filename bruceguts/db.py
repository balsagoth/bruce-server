import os
import records
import logme

from .env import DATABASE_URL, SQL_PATH, SQL_SCHEMA_PATH


@logme.log
class Database:
    def __init__(self, db_url: str = None):
        self.db_url = db_url or DATABASE_URL
        self.db = records.Database(db_url=self.db_url)

        if self.is_fresh:
            self.migrate()

    @property
    def config(self):
        return self.db.query("SELECT * FROM config;").first(as_dict=True, default={})

    @config.setter
    def config(self, other):
        # Make sure this is a dictionary.
        assert hasattr(other, "keys")

        for item in other:
            self.db.query("UPDATE config SET :k = :v", k=item, v=other[item])

    @property
    def schemas(self):
        # Get the schemas.
        for root, _, files in os.walk(SQL_SCHEMA_PATH):
            for _file in files:
                yield f"{root}/{_file}"

    def migrate(self):
        self.logger.info("Initializing database!")

        for schema in sorted(self.schemas):
            self.logger.info(f"Applying {schema!r}!")

            self.db.query_file(schema)

            self.logger.info(f"Applied {schema!r}!")

    @property
    def is_fresh(self):
        self.logger.info("Checking for tables...")
        q = """
            SELECT
                table_name FROM information_schema.tables
            WHERE
                table_type='BASE TABLE' AND table_schema='public';
        """
        return not bool(len(self.db.query(q, fetchall=True)))

    @property
    def apps(self):
        self.logger.info("Checking for apps...")
        # return []
        return self.db.query("SELECT * from apps;", fetchall=True)


db = Database(db_url=DATABASE_URL)
