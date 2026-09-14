from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .routers import auth, health

settings.validate_jwt_secret()

app = FastAPI(title='Authentication API')
app.add_middleware(CORSMiddleware, allow_origins=[settings.frontend_url], allow_credentials=True, allow_methods=['GET', 'POST'], allow_headers=['Content-Type'])
app.include_router(health.router); app.include_router(auth.router)

@app.get('/api/cicd-test')
def cicd_test(): return {'message': 'CI/CD deployment successful'}

@app.get('/api/deployment-status')
def deployment_status():
	return {'message': 'Backend deployment is running the latest code', 'status': 'ok'}