import pytest
from server.benzai_api import app
from werkzeug.test import Client


@pytest.fixture()
def client():
    return Client(app)
