from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .routers import auth, health

settings.validate_jwt_secret()

app = FastAPI(title="Authentication API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://aws-phi-neon.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(auth.router)
