import jwt
from fastapi import Cookie, HTTPException, status
from .config import settings

def current_user_id(auth_token: str | None = Cookie(default=None)):
    if not auth_token: raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication required.')
    try: return int(jwt.decode(auth_token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])['sub'])
    except (jwt.InvalidTokenError, KeyError, ValueError): raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid or expired authentication token.')