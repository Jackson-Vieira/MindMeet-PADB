from psycopg import Connection

from app.schemas.appointment import AppointmentRequest

CREATE_REQUEST_APPOINTMENT_SQL = "INSERT INTO requests_appointments (agenda_day_hour_id, status, reason, anonymous) VALUES (%(agenda_day_hour_id)s, %(status)s, %(reason)s), %(anonymous)s"
DELETE_REQUEST_APPOINTMENT_SQL = "DELETE FROM requests_appointments WHERE id = %(id)s"
SELECT_ALL_REQUESTS_APPOINTMENTS_SQL = "SELECT * FROM requests_appointments"

class RequestAppointmentUseCases:
    def __init__(self, db_connection: Connection) -> None:
        self.db_connection = db_connection
         # TODO: make a generator to get the cursor and close it after the use
        self.cursor = self.db_connection.cursor()

    def get_all_requests_appointments(self) -> list[AppointmentRequest]:
        self.cursor.execute(SELECT_ALL_REQUESTS_APPOINTMENTS_SQL)
        requests_appointments = self.cursor.fetchall()
        return [AppointmentRequest(
            id=request_appointment[0],
            agenda_day_hour_id=request_appointment[1],
            status=request_appointment[2],
            reason=request_appointment[3],
            anonymous=request_appointment[4],
            created_at=request_appointment[5],
            updated_at=request_appointment[6])
        for request_appointment in requests_appointments]
    
    def create_request_appointment(self, appoiment_request: AppointmentRequest) -> None:
        self.cursor.execute(CREATE_REQUEST_APPOINTMENT_SQL, appoiment_request.model_dump())
        self.db_connection.commit()

    def delete_request_appointment(self, id: int) -> None:
        self.cursor.execute(DELETE_REQUEST_APPOINTMENT_SQL, {"id": id})
        self.db_connection.commit()

    