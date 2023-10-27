from psycopg import Connection
from app.schemas.users import (UserCreate)

"""
# id SERIAL PRIMARY KEY,
# username VARCHAR(50) NOT NULL,
# email VARCHAR(100) NOT NULL,
# password VARCHAR(100) NOT NULL,
# created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
"""

GET_USERS_SQL = "SELECT * FROM users"
CREATE_USER_SQL = "INSERT INTO users (id, username, email, password, created_at) VALUES (%(id)s, %(username)s, %(email)s, %(password)s, %(created_at)s)"

class UserUseCases:
    def __init__(self, db_connection: Connection) -> None:
        self.db_connection = db_connection
        self.cursor = self.db_connection.cursor()

    def get_all_users(self) -> list:
        users = self.cursor.execute(GET_USERS_SQL).fetchall()
        return users
    
    def create_user(self, create_user: UserCreate) -> None:
        with self.db_connection.cursor() as cursor:
            cursor.execute(CREATE_USER_SQL, create_user.model_dump())
            self.db_connection.commit()