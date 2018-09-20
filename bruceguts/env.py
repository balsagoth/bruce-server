import os
from pathlib import Path

# print(os.environ)
# exit()

CELERY_BROKER = os.environ.get("CELERY_BROKER")
DATABASE_URL = os.environ.get("DATABASE_URL")
SQL_PATH = (Path(__file__).parent.parent / "sql").resolve()
SQL_SCHEMA_PATH = SQL_PATH / "schema"
BUILDPACKS_DIR = (Path(__file__).parent.parent / "var/buildpacks").resolve()
HEROKUISH_IMAGE = "gliderlabs/herokuish"
