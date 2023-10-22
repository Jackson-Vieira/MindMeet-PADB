import psycopg
from decouple import config

from app.database.sqls import CREATE_TABLE_USERS

POSTGRES_URI = config('POSTGRES_URI')

def get_db_connection():
    try:
        connection = psycopg.connect(POSTGRES_URI)
        yield connection
    finally:
        connection.close()

def start_db():
    with psycopg.connect(POSTGRES_URI) as conn:
        with conn.cursor() as cur:
            for sql in [CREATE_TABLE_USERS]:
                cur.execute(sql)
            conn.commit()