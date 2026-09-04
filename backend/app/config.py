import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

ENV_FILE = Path(__file__).resolve().parents[1] / '.env'
load_dotenv(ENV_FILE)


def _env_value(name, default=None):
    value = os.getenv(name)
    return default if value is None else value.strip()


def _port_value():
    raw_port = _env_value('DB_PORT', '5432')
    try:
        return int(raw_port)
    except ValueError as error:
        raise RuntimeError('DB_PORT must be a valid integer.') from error


@dataclass(frozen=True)
class Settings:
    database_host: str = _env_value('DB_HOST', 'localhost')
    database_port: int = _port_value()
    database_name: str = _env_value('DB_NAME')
    database_user: str = _env_value('DB_USER')
    database_password: str = _env_value('DB_PASSWORD')
    jwt_secret_key: str = os.getenv('JWT_SECRET_KEY', '')
    jwt_algorithm: str = os.getenv('JWT_ALGORITHM', 'HS256')
    jwt_expire_minutes: int = int(os.getenv('JWT_EXPIRE_MINUTES', '60'))
    frontend_url: str = os.getenv('FRONTEND_URL', 'http://localhost:5173')

    def database_connection_kwargs(self):
        required = {
            'DB_NAME': self.database_name,
            'DB_USER': self.database_user,
            'DB_PASSWORD': self.database_password,
        }
        missing = [name for name, value in required.items() if not value]
        if missing:
            names = ', '.join(missing)
            raise RuntimeError(
                f'Missing required database environment variables: {names}. '
                'Set them in backend/.env or the deployment environment.'
            )
        return {
            'host': self.database_host,
            'port': self.database_port,
            'dbname': self.database_name,
            'user': self.database_user,
            'password': self.database_password,
        }

    def validate_jwt_secret(self):
        if len(self.jwt_secret_key.encode('utf-8')) < 32:
            raise RuntimeError('JWT_SECRET_KEY must be at least 32 bytes long.')

    @property
    def secure_cookies(self):
        return self.frontend_url.startswith('https://')

settings = Settings()