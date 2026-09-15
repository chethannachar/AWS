from fastapi.testclient import TestClient
from app.main import app
from app.routers.auth import present

def test_me_requires_authentication():
    assert TestClient(app).get('/api/auth/me').status_code == 401

def test_login_response_includes_authenticated_user_name():
    assert present((7, 'Ada Lovelace', 'ada@example.com', None))['name'] == 'Ada Lovelace'