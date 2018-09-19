from pathlib import Path
from bruceguts import db


def test_db_schemas(mock_db_object):
    db_ = db.Database('blah')

    assert Path(sorted(db_.schemas)[0]).parts[-1] == '000.sql'
