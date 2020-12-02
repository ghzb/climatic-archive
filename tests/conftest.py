import pytest
from src.main import app

@pytest.fixture(scope='module')
def www():
    flask_app = app
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()
