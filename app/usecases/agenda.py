from psycopg import Connection

from app.schemas.agenda import Agenda, AgendaOutput

CREATE_AGENDA_SQL = "INSERT INTO agenda DEFAULT VALUES"
SELECT_ALL_AGENDAS_SQL = "SELECT * FROM agenda"
DELETE_AGENDA_SQL = "DELETE FROM agenda WHERE id = %(id)s"
SELECT_AGENDA_SQL = "SELECT * FROM agenda WHERE id = %(id)s"

class AgendaUseCases:
    def __init__(self, db_connection: Connection) -> None:
        self.db_connection = db_connection
        # TODO: make a generator to get the cursor and close it after the use
        self.cursor = self.db_connection.cursor()

    def create_agenda(self, agenda: Agenda) -> None:
        self.cursor.execute(CREATE_AGENDA_SQL)
        self.db_connection.commit()

    def get_agenda_by_id(self, id: int) -> AgendaOutput:
        self.cursor.execute(SELECT_AGENDA_SQL, {"id": id})
        agenda = self.cursor.fetchone() 
        return AgendaOutput(id=agenda[0], start_datetime=agenda[1], end_datetime=agenda[2])

    def get_all_agendas(self) -> list[Agenda]:
        self.cursor.execute(SELECT_ALL_AGENDAS_SQL)
        agendas = self.cursor.fetchall()
        return [AgendaOutput(id=agenda[0], start_datetime=agenda[1], end_datetime=agenda[2]) for agenda in agendas]