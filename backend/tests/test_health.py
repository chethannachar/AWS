from fastapi.testclient import TestClient
from app.main import app

def test_root_deployment_message():
    assert TestClient(app).get('/').json() == {
        'message': 'CI/CD pipeline deployed the latest backend code',
    }

def test_health():
    assert TestClient(app).get('/api/health').json() == {'status': 'ok'}

def test_cicd_test():
    assert TestClient(app).get('/api/cicd-test').json() == {'message': 'CI/CD deployment successful'}

def test_deployment_status():
    assert TestClient(app).get('/api/deployment-status').json() == {
        'message': 'Backend deployment is running the latest code',
        'status': 'ok',
    }