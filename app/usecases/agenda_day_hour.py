from app.schemas.agenda import AgendaDayHour, AgendaDayHourOutput

from .base import BaseUseCase

CREATE_AGENDA_DAY_HOUR_SQL = "INSERT INTO agenda_day_hour (agenda_id, start_date_time, end_date_time) VALUES (%(agenda_id)s, %(start_date_time)s, %(end_date_time)s)"
SELECT_ALL_AGENDAS_DAY_HOUR_SQL = "SELECT id, agenda_id, start_date_time, end_date_time FROM agenda_day_hour WHERE agenda_id = %(agenda_id)s"
UPDATE_AGENDA_DAY_HOUR_SQL = "UPDATE agenda_day_hour SET start_date_time = %(start_date_time)s, end_date_time = %(end_date_time)s WHERE id = %(id)s"

class AgendaDayHourUseCases(BaseUseCase):
    def create_agenda_day_hour(self, agenda_id, agenda_day_hour:AgendaDayHour) -> None:
        with self.db_connection.cursor() as cursor:
            cursor.execute(CREATE_AGENDA_DAY_HOUR_SQL, {
                "id": agenda_id, 
                **agenda_day_hour.model_dump()
            })
            self.db_connection.commit()

    def update_agenda_day_hour(self, id: int, agenda_day_hour: AgendaDayHour) -> None:
        with self.db_connection.cursor() as cursor:
            cursor.execute(UPDATE_AGENDA_DAY_HOUR_SQL, {"id": id, **agenda_day_hour.model_dump()})
            self.db_connection.commit()

    def filter_agendas_day_hour_by_agenda_id(self, agenda_id) -> list[AgendaDayHour]:
        with self.db_connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_AGENDAS_DAY_HOUR_SQL, {"agenda_id": agenda_id})
            agendas_day_hour = cursor.fetchall()
            return [AgendaDayHourOutput(id=agenda_day_hour[0], agenda_id=agenda_day_hour[1], start_date_time=agenda_day_hour[2], end_date_time=agenda_day_hour[3]) for agenda_day_hour in agendas_day_hour]