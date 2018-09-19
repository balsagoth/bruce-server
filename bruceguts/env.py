import os
from pathlib import Path

CELERY_BROKER = os.environ.get("CELERY_BROKER")
DATABASE_URL = os.environ.get("DATABASE_URL")
SQL_PATH = (Path(__file__).parent.parent / "sql").resolve()
SQL_SCHEMA_PATH = SQL_PATH / "schema"
