from psycopg import Connection

from app.schemas.agenda import AgendaDayHour

CREATE_AGENDA_DAY_HOUR_SQL = "INSERT INTO agenda_day_hour (agenda_id, start_date_time, end_date_time) VALUES (%(agenda_id)s, %(start_date_time)s, %(end_date_time)s)"
SELECT_ALL_AGENDAS_DAY_HOUR_SQL = "SELECT (id, start_datetime, end_datetime) FROM agenda_day_hour WHERE agenda_id = %(agenda_id)s"
UPDATE_AGENDA_DAY_HOUR_SQL = "UPDATE agenda_day_hour SET start_date_time = %(start_date_time)s, end_date_time = %(end_date_time)s WHERE id = %(id)s"

class AgendaDayHourUseCases:
    def __init__(self, db_connection: Connection) -> None:
        self.db_connection = db_connection
        # TODO: make a generator to get the cursor and close it after the use
        self.cursor = self.db_connection.cursor()

    def create_agenda_day_hour(self, agenda_day_hour:AgendaDayHour ) -> None:
        self.cursor.execute(CREATE_AGENDA_DAY_HOUR_SQL, agenda_day_hour.model_dump())
        self.db_connection.commit()

    def update_agenda_day_hour(self, id: int, start_date_time: str, end_date_time: str) -> None:
        self.cursor.execute(UPDATE_AGENDA_DAY_HOUR_SQL, {"id": id, "start_date_time": start_date_time, "end_date_time": end_date_time})
        self.db_connection.commit()

    def get_all_agendas_day_hour_by_agenda_id(self, agenda_id) -> list[AgendaDayHour]:
        self.cursor.execute(SELECT_ALL_AGENDAS_DAY_HOUR_SQL, {"agenda_id": agenda_id})
        agendas_day_hour = self.cursor.fetchall()
        return [AgendaDayHour(id=agenda_day_hour[0], start_datetime=agenda_day_hour[1], end_datetime=agenda_day_hour[2]) for agenda_day_hour in agendas_day_hour]
