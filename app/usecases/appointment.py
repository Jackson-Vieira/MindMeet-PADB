# from datetime import datetime
from app.schemas.appointment import AppointmentCreate, AppointmentOutput

from .base import BaseUseCase

CREATE_APPOINTMENT_SQL = "INSERT INTO appointments (status, reason, anonymous, agenda_day_hour_id, psychologist_id, patient_id) VALUES (%(status)s, %(reason)s, %(anonymous)s, %(agenda_day_hour_id)s)"
UPDATE_APPOINTMENT_SQL = "UPDATE appointments SET status = %(status)s, reason = %(reason)s, anonymous = %(anonymous)s, agenda_day_hour_id = %(agenda_day_hour_id)s WHERE id = %(id)s"
SELECT_ALL_APPOINTMENTS_SQL = "SELECT id, agenda_day_hour_id, status, reason, anonymous, created_at, updated_at, psychologist_id, patient_id FROM appointments"
SELECT_APPOINTMENT_SQL = "SELECT id, agenda_day_hour, status, reason, anonymous, created_at, updated_at, psychologist_id, patient_id FROM appointments WHERE id = %(id)s"
DELETE_APPOINTMENT_SQL = "DELETE FROM appointments WHERE id = %(id)s"

class AppointmentUseCases(BaseUseCase):
    def get_all_appointments(self) -> list[AppointmentOutput]:
        with self.db_connection.cursor() as cursor:
            cursor.execute(SELECT_ALL_APPOINTMENTS_SQL)
            appointment = cursor.fetchall()
            return [AppointmentOutput(
                id=appoiment[0],
                agenda_day_hour_id=appoiment[1],
                status=appoiment[2],
                reason=appoiment[3],
                anonymous=appoiment[4],
                created_at=appoiment[5],
                updated_at=appoiment[6],
                psychologist_id=appoiment[7],
                patient_id=appoiment[8],
            )
            for appoiment in appointment]

    
    def get_appointments_by_id(self, id: int) -> AppointmentOutput:
        with self.db_connection.cursor() as cursor:
            cursor.execute(SELECT_APPOINTMENT_SQL, {"id": id})
            appoiment = cursor.fetchone()
            return AppointmentOutput(
                id=appoiment[0],
                agenda_day_hour_id=appoiment[1],
                status=appoiment[2],
                reason=appoiment[3],
                anonymous=appoiment[4],
                created_at=appoiment[5],
                updated_at=appoiment[6],
            )

    def create_appointment(self, appointment: AppointmentCreate) -> None:
        with self.db_connection.cursor() as cursor:
            cursor.execute(CREATE_APPOINTMENT_SQL, appointment.model_dump())
            self.db_connection.commit()

    def delete_appointment(self, id: int) -> None:
        with self.db_connection.cursor() as cursor:
            cursor.execute(DELETE_APPOINTMENT_SQL, {"id": id})
            self.db_connection.commit()

    # TODO: update updated_at when update method
    def update_appointment(self, appointment: AppointmentCreate) -> None:
        # appointment.updated_at = datetime.now() # maybe this is not the best way to do it
        with self._get_cursor() as cursor:
            cursor.execute(UPDATE_APPOINTMENT_SQL, appointment.model_dump())
            self.db_connection.commit()