from app.schemas.user import User, UserCreate

from .base import BaseUseCase

CREATE_USER_SQL = "INSERT INTO users (email, password_hash, full_name, city) VALUES (%(email)s, %(password_hash)s, %(full_name)s, %(city)s)"
SELECT_ALL_USERS_SQL = "SELECT id, email, password_hash, full_name, city, data_joined FROM users"
# DELETE_USER_SQL = "DELETE FROM users WHERE id = %(id)s"
SELECT_USER_SQL = "SELECT id, email, password_hash, full_name, city, data_joined FROM users WHERE id = %(id)s"
UPDATE_USER_SQL = "UPDATE users SET name = %(name)s, email = %(email)s, password_hash = %(password_hash)s, city = %(city)s WHERE id = %(id)s"

class AgendaUseCases(BaseUseCase):
    def create_user(self, user: UserCreate) -> None:
        user.password_hash = self._hash_password(user.password_hash)
        with self.db_connection.cursor() as cursor:
            cursor.execute(CREATE_USER_SQL, user.model_dump())
            self.db_connection.commit()
    
    def get_user_by_id(self, id: int) -> User:
        with self.db_connection.cursor() as cursor:
            cursor.execute(SELECT_USER_SQL, {"id": id})
            user = cursor.fetchone()
            return User(id=user[0], email=user[1], password_hash=user[2], full_name=user[3], city=user[4], data_joined=user[5])
    
    def get_all_users(self) -> list[User]:
        with self.db_connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_USERS_SQL)
            users = cursor.fetchall()
            return [User(id=user[0], email=user[1], password_hash=user[2], full_name=user[3], city=user[4], data_joined=user[5]) for user in users]
    
    # def delete_user(self, id: int) -> None:
    #     with self.db_connection.cursor() as cursor:
    #         cursor.execute(DELETE_USER_SQL, {"id": id})
    #         self.db_connection.commit()

    def _hash_password(self, password: str) -> str:
        return password + "fakehash"