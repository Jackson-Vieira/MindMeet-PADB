from app.schemas.agenda import Agenda, AgendaOutput

from .base import BaseUseCase

CREATE_AGENDA_SQL = "INSERT INTO agenda DEFAULT VALUES"
SELECT_ALL_AGENDAS_SQL = "SELECT * FROM agenda"
DELETE_AGENDA_SQL = "DELETE FROM agenda WHERE id = %(id)s"
SELECT_AGENDA_SQL = "SELECT * FROM agenda WHERE id = %(id)s"

class AgendaUseCases(BaseUseCase):
    def create_agenda(self, agenda: Agenda) -> None:
        with self.db_connection.cursor() as cursor:
            cursor.execute(CREATE_AGENDA_SQL)
            self.db_connection.commit()

    def get_agenda_by_id(self, id: int) -> AgendaOutput:
        with self.db_connection.cursor() as cursor:
            cursor.execute(SELECT_AGENDA_SQL, {"id": id})
            agenda = self.cursor.fetchone() 
            return AgendaOutput(id=agenda[0], start_datetime=agenda[1], end_datetime=agenda[2])

    def get_all_agendas(self) -> list[Agenda]:
        with self.db_connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_AGENDAS_SQL)
            agendas = cursor.fetchall()
            return [AgendaOutput(id=agenda[0], start_datetime=agenda[1], end_datetime=agenda[2]) for agenda in agendas]