from fastapi import APIRouter

router = APIRouter()

@router.get('/api/health')
def health():
    return {"status": "ok"}

@router.get('/api/app-info')
def app_info():
    return {
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