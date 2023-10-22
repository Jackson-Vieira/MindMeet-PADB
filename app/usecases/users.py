from psycopg import Connection

GET_USERS_SQL = "SELECT * FROM users"

class UserUseCases:
    def __init__(self, db_connection: Connection) -> None:
        self.db_connection = db_connection
        self.cursor = self.db_connection.cursor()

    def get_all_users(self) -> list:
        users = self.cursor.execute(GET_USERS_SQL).fetchall()
        return users