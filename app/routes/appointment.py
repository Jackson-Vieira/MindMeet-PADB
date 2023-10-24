from fastapi import APIRouter, Depends, Response, status
from psycopg import Connection

from app.database.connection import get_db_connection
from app.schemas.appointment import AppointmentCreate
from app.usecases.appointment import AppointmentUseCases

router = APIRouter(prefix="/appointments")


@router.get('')
def list_all(
    db_connection: Connection = Depends(get_db_connection)
):
    uc = AppointmentUseCases(db_connection)
    appointments = uc.get_all_appointments()
    return appointments
    
@router.post('')
def create_appointment(
    appointment: AppointmentCreate,
    db_connection: Connection = Depends(get_db_connection)
):
    uc = AppointmentUseCases(db_connection)
    uc.create_appointment(appointment)
    return Response(status_code=status.HTTP_201_CREATED)

@router.get('/{appointment_id}')
def get_appointment(
    appointment_id: int,
    db_connection: Connection = Depends(get_db_connection)
):
    uc = AppointmentUseCases(db_connection)
    appointment = uc.get_appointment(appointment_id)
    return appointment

@router.put('/{appointment_id}')
def update_appointment(
    appointment_id: int,
    appointment: AppointmentCreate,
    db_connection: Connection = Depends(get_db_connection)
):
    uc = AppointmentUseCases(db_connection)
    uc.update_appointment(appointment_id, appointment)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.delete('/{appointment_id}')
def delete_appointment(
    appointment_id: int,
    db_connection: Connection = Depends(get_db_connection)
):
    uc = AppointmentUseCases(db_connection)
    uc.delete_appointment(appointment_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
