from psycopg import Connection

from app.schemas.appoiment import AppoimentCreate
from app.usecases.appoiments import (
    SELECT_ALL_APPOINMENTS_SQL,
    AppointmentUseCase,
)


def test_create_appointment(db_connection: Connection):
    uc = AppointmentUseCase()
    
    appointment = AppoimentCreate(
        status=True,
        description="test description",
        reason="test",
        anonymous=False,
        agenda_day_hour_id=1,
        psychologist_id=1,
        patient_id=1,
    )

    appointment = uc.create_appointment(appointment)
    appointments_on_db = db_connection.execute(SELECT_ALL_APPOINMENTS_SQL).fetchall()
    assert len(appointments_on_db) == 1
    assert appointments_on_db[0]['psychologist_id'] == 1
    assert appointments_on_db[0]['patient_id'] == 1
    assert appointments_on_db[0]['agenda_day_hour_id'] == 1


def test_get_all_appointments(db_connection: Connection):
    uc = AppointmentUseCase()
    appointments = uc.get_all_appointments()
    appointments_on_db = db_connection.execute(SELECT_ALL_APPOINMENTS_SQL).fetchall()
    assert len(appointments) == len(appointments_on_db)
    assert appointments[0].id == appointments_on_db[0]['id']

def test_get_appointment_by_id(db_connection: Connection):
    uc = AppointmentUseCase()
    appointment = AppoimentCreate(
        status=True,
        description="test description",
        reason="test",
        anonymous=False,
        agenda_day_hour_id=1,
        psychologist_id=1,
        patient_id=1,
    )
    appointment = uc.create_appointment(appointment)
    appointment_on_db = uc.get_appointment_by_id(appointment.id)
    assert appointment_on_db.id == appointment.id
    assert appointment_on_db.status == appointment.status
    assert appointment_on_db.description == appointment.description
    assert appointment_on_db.reason == appointment.reason
    assert appointment_on_db.anonymous == appointment.anonymous
    assert appointment_on_db.agenda_day_hour_id == appointment.agenda_day_hour_id
    assert appointment_on_db.psychologist_id == appointment.psychologist_id
    assert appointment_on_db.patient_id == appointment.patient_id

def test_delete_appointment(db_connection: Connection):
    uc = AppointmentUseCase()
    appointment = AppoimentCreate(
        status=True,
        description="test description",
        reason="test",
        anonymous=False,
        agenda_day_hour_id=1,
        psychologist_id=1,
        patient_id=1,
    )
    appointment = uc.create_appointment(appointment)
    appointments_on_db = db_connection.execute(SELECT_ALL_APPOINMENTS_SQL).fetchall()
    assert len(appointments_on_db) == 1
    assert appointments_on_db[0]['psychologist_id'] == 1
    assert appointments_on_db[0]['patient_id'] == 1
    assert appointments_on_db[0]['agenda_day_hour_id'] == 1

    uc.delete_appointment(appointment.id)
    appointments_on_db = db_connection.execute(SELECT_ALL_APPOINMENTS_SQL).fetchall()
    assert len(appointments_on_db) == 0

def test_update_appointment(db_connection: Connection):
    uc = AppointmentUseCase()
    appointment = AppoimentCreate(
        status=False,
        description="test description",
        reason="test",
        anonymous=False,
        agenda_day_hour_id=1,
        psychologist_id=1,
        patient_id=1,
    )
    appointment = uc.create_appointment(appointment)
    appointments_on_db = db_connection.execute(SELECT_ALL_APPOINMENTS_SQL).fetchall()
    assert len(appointments_on_db) == 1
    assert appointments_on_db[0]['psychologist_id'] == 1
    assert appointments_on_db[0]['patient_id'] == 1
    assert appointments_on_db[0]['agenda_day_hour_id'] == 1

    appointment = AppoimentCreate(
        status=True,
        description="test description updated",
        reason="test",
        anonymous=False,
        agenda_day_hour_id=1,
        psychologist_id=1,
        patient_id=1,
    )

    appointment = uc.update_appointment(appointment)
    appointments_on_db = db_connection.execute(SELECT_ALL_APPOINMENTS_SQL).fetchall()
    assert len(appointments_on_db) == 1
    assert appointments_on_db[0]['psychologist_id'] == 1
    assert appointments_on_db[0]['patient_id'] == 1
    assert appointments_on_db[0]['agenda_day_hour_id'] == 1
    assert appointments_on_db[0]['status']
    assert appointments_on_db[0]['description'] == "test description updated"