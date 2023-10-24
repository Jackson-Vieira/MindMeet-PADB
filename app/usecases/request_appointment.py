from app.schemas.appointment import (
    AppointmentRequestCreate,
    AppointmentRequestOutput,
)

from .base import BaseUseCase

CREATE_REQUEST_APPOINTMENT_SQL = "INSERT INTO requests_appointments (agenda_day_hour_id, status, reason) VALUES (%(agenda_day_hour_id)s, %(status)s, %(reason)s)"
DELETE_REQUEST_APPOINTMENT_SQL = "DELETE FROM requests_appointments WHERE id = %(id)s"
SELECT_ALL_REQUESTS_APPOINTMENTS_SQL = "SELECT id, agenda_day_hour_id, status, reason, created_at, updated_at FROM requests_appointments"

class RequestAppointmentUseCases(BaseUseCase):
    def get_all_requests_appointments(self) -> list[AppointmentRequestOutput]:
        with self.db_connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_REQUESTS_APPOINTMENTS_SQL)
            requests_appointments = cursor.fetchall()
            return [AppointmentRequestOutput(
                id=request_appointment[0],
                agenda_day_hour_id=request_appointment[1],
                status=request_appointment[2],
                reason=request_appointment[3],
                created_at=request_appointment[4],
                updated_at=request_appointment[5])
            for request_appointment in requests_appointments]
    
    def create_request_appointment(self, appoiment_request: AppointmentRequestCreate) -> None:
        with self.db_connection.cursor() as cursor:
            cursor.execute(CREATE_REQUEST_APPOINTMENT_SQL, appoiment_request.model_dump())
            self.db_connection.commit()

    def delete_request_appointment(self, id: int) -> None:
        with self.db_connection.cursor() as cursor:
            cursor.execute(DELETE_REQUEST_APPOINTMENT_SQL, {"id": id})
            self.db_connection.commit()