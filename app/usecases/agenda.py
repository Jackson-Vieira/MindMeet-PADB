from psycopg import Connection

from app.schemas.agenda import Agenda, AgendaOutput
from app.schemas.appointment import AppointmentRequest

# make appoiment create sql and update sql
CREATE_AGENDA_SQL = "INSERT INTO agenda DEFAULT VALUES"
SELECT_ALL_AGENDAS_SQL = "SELECT * FROM agenda"
DELETE_AGENDA_SQL = "DELETE FROM agenda WHERE id = %(id)s"
SELECT_AGENDA_SQL = "SELECT * FROM agenda WHERE id = %(id)s"

CREATE_AGENDA_DAY_HOUR_SQL = "INSERT INTO agenda_day_hour (agenda_id, start_date_time, end_date_time) VALUES (%(agenda_id)s, %(start_date_time)s, %(end_date_time)s)"
SELECT_ALL_AGENDAS_DAY_HOUR_SQL = "SELECT * FROM agenda_day_hour"
UPDATE_AGENDA_DAY_HOUR_SQL = "UPDATE agenda_day_hour SET start_date_time = %(start_date_time)s, end_date_time = %(end_date_time)s WHERE id = %(id)s"

# move to appointment usecases
CREATE_REQUEST_APPOINTMENT_SQL = "INSERT INTO requests_appointments (agenda_day_hour_id, status, reason, anonymous) VALUES (%(agenda_day_hour_id)s, %(status)s, %(reason)s), %(anonymous)s"
UPDATE_REQUEST_APPOINTMENT_SQL = "UPDATE requests_appointments SET status = %(status)s WHERE id = %(id)s"
DELETE_REQUEST_APPOINTMENT_SQL = "DELETE FROM requests_appointments WHERE id = %(id)s"
SELECT_ALL_REQUESTS_APPOINTMENTS_SQL = "SELECT * FROM requests_appointments"

format_string = '%Y-%m-%d %H:%M:%S'

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
        return AgendaOutput(id=agenda[0], start_datetime=agenda[1], end_datetime=agenda[2])

    def get_all_agendas(self) -> list[Agenda]:
        self.cursor.execute(SELECT_ALL_AGENDAS_SQL)
        agendas = self.cursor.fetchall()
        return [AgendaOutput(id=agenda[0], start_datetime=agenda[1], end_datetime=agenda[2]) for agenda in agendas]
    
    def create_request_appointment(self, appoiment_request: AppointmentRequest) -> None:
        self.cursor.execute(CREATE_REQUEST_APPOINTMENT_SQL, appoiment_request.model_dump())
        self.db_connection.commit()
    
    # def create_agenda_day_hour(self, agenda_id: int, start_date_time: str, end_date_time: str) -> None:
    #     self.cursor.execute(CREATE_AGENDA_DAY_HOUR_SQL, {"agenda_id": agenda_id, "start_date_time": start_date_time, "end_date_time": end_date_time})
    #     self.db_connection.commit()

    # def update_agenda_day_hour(self, id: int, start_date_time: str, end_date_time: str) -> None:
    #     self.cursor.execute(UPDATE_AGENDA_DAY_HOUR_SQL, {"id": id, "start_date_time": start_date_time, "end_date_time": end_date_time})
    #     self.db_connection.commit()
