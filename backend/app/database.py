from contextlib import contextmanager
import psycopg
from .config import settings

def connection_string():
    return settings.database_connection_kwargs()

@contextmanager
def get_connection():
    with psycopg.connect(**connection_string()) as connection:
        yield connection