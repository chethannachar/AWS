from fastapi import APIRouter, Depends, Response, status
from ..dependencies import current_user_id
from ..schemas.auth import LoginRequest, RegisterRequest, UserResponse
from ..services.auth import authenticate, create_token, create_user, find_user
from ..config import settings

router = APIRouter(prefix='/api/auth')
def present(user): return {'id': user[0], 'name': user[1], 'email': user[2], 'created_at': user[3]}

@router.post('/register', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(payload: RegisterRequest): return present(create_user(payload.name.strip(), payload.email.lower(), payload.password))

@router.post('/login', response_model=UserResponse)
def login(payload: LoginRequest, response: Response):
    user = authenticate(payload.email.lower(), payload.password); response.set_cookie('auth_token', create_token(user[0]), httponly=True, secure=settings.secure_cookies, samesite='none' if settings.secure_cookies else 'lax', max_age=3600 * 24)
    return present(user)

@router.get('/me', response_model=UserResponse)
def me(user_id: int = Depends(current_user_id)):
    user = find_user(user_id)
    if not user: from fastapi import HTTPException; raise HTTPException(status_code=401, detail='User account not found.')
    return present(user)

@router.post('/logout')
def logout(response: Response): response.delete_cookie('auth_token', httponly=True, secure=settings.secure_cookies, samesite='none' if settings.secure_cookies else 'lax'); return {'message': 'Logged out.'}