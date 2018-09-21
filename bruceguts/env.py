import os
import tempfile
from pathlib import Path

# print(os.environ)
# exit()

CELERY_BROKER = os.environ["CELERY_BROKER"]
DATABASE_URL = os.environ["DATABASE_URL"]
MINIO_ACCESS_KEY = os.environ["MINIO_ACCESS_KEY"]
MINIO_SECRET_KEY = os.environ["MINIO_SECRET_KEY"]
MINIO_URL = os.environ["MINIO_URL"]
SQL_PATH = (Path(__file__).parent.parent / "sql").resolve()
SQL_SCHEMA_PATH = SQL_PATH / "schema"
# BUILDPACKS_DIR = tempfile.mkdtemp()
HEROKUISH_IMAGE = "gliderlabs/herokuish"
