from psycopg import Connection
from app.schemas.users import (UserCreate, User)

"""
# id SERIAL PRIMARY KEY,
# username VARCHAR(50) NOT NULL,
# email VARCHAR(100) NOT NULL,
# password VARCHAR(100) NOT NULL,
# created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
"""

GET_USERS_SQL = "SELECT * FROM users"
CREATE_USER_SQL = "INSERT INTO users (id, username, email, password, created_at) VALUES (%(id)s, %(username)s, %(email)s, %(password)s, %(created_at)s)"
DELETE_USER_SQL = "DELETE FROM users WHERE id = %(id)s"
GET_USER_ID_SQL = "SELECT (id, username, email, password, created_at) FROM users WHERE id = %(id)s"
UPDATE_USER_SQL = "UPDATE users SET username = %(username)s, email = %(email)s, password = %(password)s, created_at = %(created_at)s WHERE id = %(id)s"


class UserUseCases:
    def __init__(self, db_connection: Connection) -> None:
        self.db_connection = db_connection
        self.cursor = self.db_connection.cursor()

    def get_all_users(self) -> list:
        users = self.cursor.execute(GET_USERS_SQL).fetchall()
        return users
   
    def get_user_id(self, id: int) -> list [User]:
        with self.db_connection.cursor() as cursor:
            cursor.execute(GET_USER_ID_SQL, {"id": id})
            user = cursor.fetchone()
            return [User(
                id=user[0],
                username=user[1],
                email=user[2],
                password=user[3],
                created_at=user[4],
            ) for user in user]
        
    
    def create_user(self, create_user: UserCreate) -> None:
        with self.db_connection.cursor() as cursor:
            cursor.execute(CREATE_USER_SQL, create_user.model_dump())
            self.db_connection.commit()
    
    def delete_user_id(self, id: int): 
        with self.db_connection.cursor() as cursor:
            cursor.execute(DELETE_USER_SQL, {"id": id})
            self.db_connection.commit()

    def update_user(self,user_id: int, user: UserCreate) -> None:
        with self.db_connection.cursor() as cursor:
            cursor.execute(UPDATE_USER_SQL, user.model_dump())
            self.db_connection.commit()
        return User