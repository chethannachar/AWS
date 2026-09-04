from datetime import datetime, timedelta, timezone
import bcrypt
import jwt
from fastapi import HTTPException, status
from ..config import settings
from ..database import get_connection

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password, password_hash):
    return bcrypt.checkpw(password.encode(), password_hash.encode())

def create_token(user_id):
    expires = datetime.now(timezone.utc) + timedelta(minutes=settings.jwt_expire_minutes)
    return jwt.encode({'sub': str(user_id), 'exp': expires}, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)

def create_user(name, email, password):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT id FROM users WHERE email = %s', (email,))
            if cursor.fetchone(): raise HTTPException(status_code=409, detail='An account with this email already exists.')
            cursor.execute('INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s) RETURNING id, name, email, created_at', (name, email, hash_password(password)))
            return cursor.fetchone()

def authenticate(email, password):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT id, name, email, password_hash, created_at FROM users WHERE email = %s', (email,))
            user = cursor.fetchone()
    if not user or not verify_password(password, user[3]): raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid email or password.')
    return user[0], user[1], user[2], user[4]

def find_user(user_id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT id, name, email, created_at FROM users WHERE id = %s', (user_id,))
            return cursor.fetchone()