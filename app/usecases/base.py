from psycopg import Connection


class BaseUseCase:
    def __init__(self, db_connection: Connection) -> None:
        self.db_connection = db_connection