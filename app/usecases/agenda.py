import logging

from psycopg import Connection

from app.schemas.agenda import Agenda, AgendaOutput

# make appoiment create sql and update sql
CREATE_AGENDA_SQL = "INSERT INTO agenda DEFAULT VALUES;"
SELECT_ALL_AGENDAS_SQL = "SELECT * FROM agenda"
DELETE_AGENDA_SQL = "DELETE FROM agenda WHERE id = %(id)s"
SELECT_AGENDA_SQL = "SELECT * FROM agenda WHERE id = %(id)s"

class AgendaUseCases:
    def __init__(self, db_connection: Connection) -> None:
        self.db_connection = db_connection
        self.cursor = self.db_connection.cursor()

    def create_agenda(self, agenda: Agenda) -> None:
        self.cursor.execute(CREATE_AGENDA_SQL)
        self.db_connection.commit()

    def get_agenda_by_id(self, id: int) -> AgendaOutput:
        self.cursor.execute(SELECT_AGENDA_SQL, {"id": id})
        agenda = self.cursor.fetchone()
        return AgendaOutput(id=agenda[0])

    def get_all_agendas(self) -> list[Agenda]:
        self.cursor.execute(SELECT_ALL_AGENDAS_SQL)
        agendas = self.cursor.fetchall()
        return agendas