from fastapi import APIRouter, Depends
from psycopg import Connection

from app.database.connection import get_db_connection
from app.usecases.appointment import AppointmentUseCases

router = APIRouter(prefix="/appointments")


@router.get('')
def list_all(
    db_connection: Connection = Depends(get_db_connection)
):
    uc = AppointmentUseCases(db_connection)
    appointments = uc.get_all_appointments()
    return appointments
    