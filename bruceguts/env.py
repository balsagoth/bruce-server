import os

CELERY_BROKER = os.environ["CELERY_BROKER"]
DATABASE_URL = os.environ["DATABASE_URL"]
SQL_PATH = os.path.abspath(os.path.join([os.path.dirname(__file__), "..", "sql"]))
SQL_SCHEMA_PATH = os.path.join([SQL_PATH, SQL_SCHEMA_PATH])
