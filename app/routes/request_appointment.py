from fastapi import APIRouter, Depends, Response, status
from psycopg import Connection

from app.database.connection import get_db_connection
from app.schemas.appointment import AppointmentRequestCreate

# from app.schemas.appointment import AppointmentRequestCreate, AppointmentRequestOutput
from app.usecases.request_appointment import RequestAppointmentUseCases

router = APIRouter(prefix="/request-appointments")

@router.get('')
def list_all(
    db_connection: Connection = Depends(get_db_connection)
):
    uc = RequestAppointmentUseCases(db_connection)
    appointments = uc.get_all_requests_appointments()
    return appointments

@router.post('')
@router.get('')
def create_request_appointment(
    request_appointment: AppointmentRequestCreate,
    db_connection: Connection = Depends(get_db_connection)
):
    uc = RequestAppointmentUseCases(db_connection)
    uc.create_request_appointment(appoiment_request=request_appointment)
    return Response(content="sucess", status_code=status.HTTP_201_CREATED)