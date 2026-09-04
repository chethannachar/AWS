from fastapi.testclient import TestClient
from app.main import app

def test_me_requires_authentication():
    assert TestClient(app).get('/api/auth/me').status_code == 401