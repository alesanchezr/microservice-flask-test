import os, pytest
from routes import api

@pytest.fixture
def client():
    app = api.get_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        # withapp.app_context():
            # flaskr.init_db()
        yield client

    # os.close(db_fd)
    # os.unlink(flaskr.app.config['DATABASE'])

def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'No entries here so far' in rv.data