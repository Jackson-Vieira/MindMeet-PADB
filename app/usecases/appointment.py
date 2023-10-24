# from datetime import datetime

from psycopg import Connection

from app.schemas.appointment import AppointmentCreate, AppointmentOutput

CREATE_APPOINTMENT_SQL = "INSERT INTO appointments (status, reason, anonymous, agenda_day_hour_id) VALUES (%(status)s, %(reason)s, %(anonymous)s, %(agenda_day_hour_id)s)"
UPDATE_APPOINTMENT_SQL = "UPDATE appointments SET status = %(status)s, reason = %(reason)s, anonymous = %(anonymous)s, agenda_day_hour_id = %(agenda_day_hour_id)s WHERE id = %(id)s"
SELECT_ALL_APPOINTMENTS_SQL = "SELECT (id, agenda_day_hour_id, status, reason, anonymous, created_at, updated_at) FROM appointments"
SELECT_APPOINTMENT_SQL = "SELECT (id, agenda_day_hour, status, reason, anonymous, created_at, updated_at) FROM appointments WHERE id = %(id)s"
DELETE_APPOINTMENT_SQL = "DELETE FROM appointments WHERE id = %(id)s"

class AppointmentUseCases:
    def __init__(self, db_connection: Connection) -> None:
        self.db_connection = db_connection
        # TODO: make a generator to get the cursor and close it after the use
        self.cursor = self.db_connection.cursor()

    def get_all_appointments(self) -> list[AppointmentOutput]:
        self.cursor.execute(SELECT_ALL_APPOINTMENTS_SQL)
        appointment = self.cursor.fetchall()
        return [AppointmentOutput(
            id=appoiment[0],
            agenda_day_hour_id=appoiment[1],
            status=appoiment[2],
            reason=appoiment[3],
            anonymous=appoiment[4],
            created_at=appoiment[5],
            updated_at=appoiment[6])
        for appoiment in appointment]

    
    def get_appointments_by_id(self, id: int) -> AppointmentOutput:
        self.cursor.execute(SELECT_APPOINTMENT_SQL, {"id": id})
        appoiment = self.cursor.fetchone()
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
        self.cursor.execute(CREATE_APPOINTMENT_SQL, appointment.model_dump())
        self.db_connection.commit()

    def delete_appointment(self, id: int) -> None:
        self.cursor.execute(DELETE_APPOINTMENT_SQL, {"id": id})
        self.db_connection.commit()

    # TODO: improve this
    def update_appointment(self, appointment: AppointmentCreate) -> None:
        # appointment.updated_at = datetime.now() # maybe this is not the best way to do it
        self.cursor.execute(UPDATE_APPOINTMENT_SQL, appointment.model_dump())
        self.db_connection.commit()