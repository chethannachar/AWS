from fastapi import APIRouter
router = APIRouter()
@router.get('/api/health')
def health(): return {"status": "o", "version": "cicd-test-1"}
