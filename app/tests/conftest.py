import psycopg
import pytest
from decouple import config

POSTGRES_URI = config('POSTGRES_URI')

@pytest.fixture
def db_connection():
    try:
        connection = psycopg.connect(POSTGRES_URI)
        yield connection
    finally:
        connection.close()