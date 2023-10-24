
from app.schemas.agenda import Agenda, AgendaOutput
from app.usecases.agenda import (
    DELETE_AGENDA_SQL,
    SELECT_ALL_AGENDAS_SQL,
    AgendaUseCases,
)


def test_create_agenda_usecases(db_connection):
    uc = AgendaUseCases(db_connection)
    assert uc is not None

def test_add_agenda(db_connection):
    uc = AgendaUseCases(db_connection)
    agenda = Agenda()
    uc.create_agenda(agenda)
    agendas_on_db = db_connection.execute(SELECT_ALL_AGENDAS_SQL).fetchall()

    assert len(agendas_on_db) == 1

    db_connection.execute(DELETE_AGENDA_SQL, {"id": agendas_on_db[0][0]})
    db_connection.commit()

def test_get_agenda(db_connection):
    uc = AgendaUseCases(db_connection)
    agenda = Agenda()
    uc.create_agenda(agenda)
    agendas_on_db = db_connection.execute(SELECT_ALL_AGENDAS_SQL).fetchall()
    agenda = uc.get_agenda_by_id(agendas_on_db[0][0])

    assert type(agenda) == AgendaOutput
    assert agenda.id == agendas_on_db[0][0]

    db_connection.execute(DELETE_AGENDA_SQL, {"id": agendas_on_db[0][0]})
    db_connection.commit()