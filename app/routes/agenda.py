from fastapi import APIRouter, Depends, Response, status
from psycopg import Connection

from app.database.connection import get_db_connection
from app.schemas.agenda import Agenda, AgendaDayHour
from app.usecases.agenda import AgendaUseCases
from app.usecases.agenda_day_hour import AgendaDayHourUseCases

router = APIRouter(tags=["Agenda"], prefix="/agendas")

# ---- AGENDA ----

@router.post('')
def create_agenda(
    db_connection: Connection = Depends(get_db_connection)
):
    uc = AgendaUseCases(db_connection)
    uc.create_agenda(agenda=Agenda())
    return Response(status_code=status.HTTP_201_CREATED)

@router.get('')
def list_all(
    db_connection: Connection = Depends(get_db_connection)
):
    uc = AgendaUseCases(db_connection)
    agendas = uc.get_all_agendas()
    return agendas

@router.get('/{id}')
def get_by_id(id: int, db_connection: Connection = Depends(get_db_connection)):
    uc = AgendaUseCases(db_connection)
    agenda = uc.get_agenda_by_id(id)
    return agenda

@router.delete('/{id}')
def delete_by_id(id: int, db_connection: Connection = Depends(get_db_connection)):
    uc = AgendaUseCases(db_connection)
    uc.delete_agenda(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# ---- AGENDA DAY HOUR ----

@router.get('/{agenda_id}/day-hour')
def list_all_agendas_day_hour(
    agenda_id: int,
    db_connection: Connection = Depends(get_db_connection)
):
    uc = AgendaDayHourUseCases(db_connection)
    agendas_day_hour = uc.filter_agendas_day_hour_by_agenda_id(agenda_id)
    return agendas_day_hour

@router.post('/{agenda_id}/day-hour')
def create_agenda_day_hour(
    agenda_id: int,
    agenda_day_hour: AgendaDayHour,
    db_connection: Connection = Depends(get_db_connection)
):
    uc = AgendaDayHourUseCases(db_connection)
    uc.create_agenda_day_hour(agenda_id, agenda_day_hour)
    return Response(status_code=status.HTTP_201_CREATED)

@router.put('/{agenda_id}/day-hour/{id}')
def update_agenda_day_hour(
    id: int,
    agenda_day_hour: AgendaDayHour,
    db_connection: Connection = Depends(get_db_connection)
):
    uc = AgendaDayHourUseCases(db_connection)
    uc.update_agenda_day_hour(id, agenda_day_hour)
    return Response(status_code=status.HTTP_204_NO_CONTENT)