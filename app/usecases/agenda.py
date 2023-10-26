from app.schemas.agenda import Agenda, AgendaOutput

from .base import BaseUseCase

CREATE_AGENDA_SQL = "INSERT INTO agenda (psychologist_id) VALUES (%(psychologist_id)s"
SELECT_ALL_AGENDAS_SQL = "SELECT * FROM agenda"
DELETE_AGENDA_SQL = "DELETE FROM agenda WHERE id = %(id)s"
SELECT_AGENDA_SQL = "SELECT id, psychologist_id, created_at, updated_at FROM agenda WHERE id = %(id)s"

class AgendaUseCases(BaseUseCase):
    def create_agenda(self, agenda: Agenda) -> None:
        with self.db_connection.cursor() as cursor:
            cursor.execute(CREATE_AGENDA_SQL, agenda.model_dump())
            self.db_connection.commit()

    def get_agenda_by_id(self, id: int) -> AgendaOutput:
        with self.db_connection.cursor() as cursor:
            cursor.execute(SELECT_AGENDA_SQL, {"id": id})
            agenda = cursor.fetchone() 
            return AgendaOutput(id=agenda[0], psychologist_id=agenda[1], created_at=agenda[2], updated_at=agenda[3])

    def get_all_agendas(self) -> list[Agenda]:
        with self.db_connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_AGENDAS_SQL)
            agendas = cursor.fetchall()
            return [AgendaOutput(id=agenda[0], psychologist_id=agenda[1], created_at=agenda[2], updated_at=agenda[3]) for agenda in agendas]
    
    def delete_agenda(self, id: int) -> None:
        with self.db_connection.cursor() as cursor:
            cursor.execute(DELETE_AGENDA_SQL, {"id": id})
            self.db_connection.commit()