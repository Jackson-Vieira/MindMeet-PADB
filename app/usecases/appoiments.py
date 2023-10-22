from psycopg import Connection

from app.schemas.appoiment import AppoimentCreate, AppoimentOutput

# make appoiment create sql and update sql
CREATE_APPOIMENT_SQL = """
    INSERT INTO appoiments (id, apelido, nome, nascimento, stack) 
    VALUES (%(id)s, %(apelido)s, %(nome)s, %(nascimento)s, %(stack)s) 
    ON conflict (apelido) do update set 
    id = excluded.id, 
    apelido = excluded.apelido, 
    nome = excluded.nome, 
    nascimento = excluded.nascimento, 
    stack = excluded.stack
"""
SELECT_ALL_APPOIMENTS_SQL = "SELECT * FROM appoiments"
SELECT_APPOIMENT_BY_ID_SQL = "SELECT * FROM appoiments WHERE id = %(id)s"
DELETE_APPOIMENT_SQL = "DELETE FROM appoiments WHERE id = %(id)s"

class AppoimentUseCases:
    def __init__(self, db_connection: Connection) -> None:
        self.db_connection = db_connection
        self.cursor = self.db_connection.cursor()

    def get_all_appoiments(self) -> list[AppoimentOutput]:
        self.cursor.execute(SELECT_ALL_APPOIMENTS_SQL)
        appoiments = self.cursor.fetchall()
        self.cursor.close()
        return appoiments
    
    def get_appoiment_by_id(self, id: int) -> AppoimentOutput:
        self.cursor.execute(SELECT_APPOIMENT_BY_ID_SQL, {"id": id})
        appoiment = self.cursor.fetchone()
        self.cursor.close()
        return appoiment

    def create_appoiment(self, appoiment: AppoimentCreate) -> None:
        self.cursor.execute(CREATE_APPOIMENT_SQL, appoiment.model_dump())
        self.db_connection.commit()
        self.cursor.close()

    def delete_appoiment(self, id: int) -> None:
        self.cursor.execute(DELETE_APPOIMENT_SQL, {"id": id})
        self.db_connection.commit()
        self.cursor.close()

    def update_appoiment(self, appoiment: AppoimentCreate) -> None:
        self.cursor.execute(CREATE_APPOIMENT_SQL, appoiment.model_dump())
        self.db_connection.commit()
        self.cursor.close()
        
