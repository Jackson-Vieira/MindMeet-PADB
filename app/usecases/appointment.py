from psycopg import Connection

from app.schemas.appoiment import AppoimentCreate, AppoimentOutput

# make appoiment create sql and update sql
CREATE_APPOINTMENT_SQL = "INSERT INTO appointments (status, reason, anonymous, agenda_day_hour_id) VALUES (%(status)s, %(reason)s, %(anonymous)s, %(agenda_day_hour_id)s)"
UPDATE_APPOINTMENT_SQL = "UPDATE appointments SET status = %(status)s, reason = %(reason)s, anonymous = %(anonymous)s, agenda_day_hour_id = %(agenda_day_hour_id)s WHERE id = %(id)s"
SELECT_ALL_APPOINTMENTS_SQL = "SELECT * FROM appoiments"
SELECT_APPOINTMENT_SQL = "SELECT * FROM appoiments WHERE id = %(id)s"
DELETE_APPOINTMENT_SQL = "DELETE FROM appoiments WHERE id = %(id)s"

class AppointmentUseCases:
    def __init__(self, db_connection: Connection) -> None:
        self.db_connection = db_connection
        self.cursor = self.db_connection.cursor()

    def get_all_appoiments(self) -> list[AppoimentOutput]:
        self.cursor.execute(SELECT_ALL_APPOINTMENTS_SQL)
        appoiments = self.cursor.fetchall()
        return appoiments
    
    def get_appoiment_by_id(self, id: int) -> AppoimentOutput:
        self.cursor.execute(SELECT_APPOINTMENT_SQL, {"id": id})
        appoiment = self.cursor.fetchone()
        return appoiment

    def create_appoiment(self, appoiment: AppoimentCreate) -> None:
        self.cursor.execute(CREATE_APPOINTMENT_SQL, appoiment.model_dump())
        self.db_connection.commit()

    def delete_appoiment(self, id: int) -> None:
        self.cursor.execute(DELETE_APPOINTMENT_SQL, {"id": id})
        self.db_connection.commit()

    def update_appoiment(self, appoiment: AppoimentCreate) -> None:
        self.cursor.execute(UPDATE_APPOINTMENT_SQL, appoiment.model_dump())
        self.db_connection.commit()