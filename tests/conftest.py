import pytest
import mock


@pytest.fixture
def mock_db_object():
    """mock records.Database object, used for testing utility functions"""
    with mock.patch('records.Database') as _:
        yield
