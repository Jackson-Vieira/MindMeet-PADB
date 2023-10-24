from fastapi import APIRouter, Depends, Response, status
from psycopg import Connection

from app.database.connection import get_db_connection
from app.schemas.agenda import Agenda
from app.usecases.agenda import AgendaUseCases

router = APIRouter(prefix="/agendas")

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