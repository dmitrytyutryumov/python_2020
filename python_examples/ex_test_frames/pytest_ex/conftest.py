import pytest
import requests

pytest_plugins = [
    "conftest",
    "tests.fixtures",
]



@pytest.yield_fixture(autouse=True, scope='session')
def requests_session():
    session = requests.Session()
    return session
