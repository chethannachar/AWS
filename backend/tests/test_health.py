from fastapi.testclient import TestClient
from app.main import app

def test_health():
    assert TestClient(app).get('/api/health').json() == {'status': 'ok'}

def test_cicd_test():
    assert TestClient(app).get('/api/cicd-test').json() == {'message': 'CI/CD deployment successful'}