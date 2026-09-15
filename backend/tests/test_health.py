from fastapi.testclient import TestClient
from app.main import app

def test_health():
    assert TestClient(app).get('/api/health').json() == {'status': 'ok'}

def test_app_info():
    assert TestClient(app).get('/api/app-info').json() == {
        'title': 'Application Information',
        'message': 'This information is coming from the FastAPI production backend.',
        'environment': 'Production',
        'deployment_message': 'Backend feature successfully deployed through CI/CD.',
        'features': [
            'FastAPI backend',
            'PostgreSQL database',
            'AWS production deployment',
        ],
    }