from datetime import datetime

from app.schemas.agenda import AgendaDayHour, AgendaOutput


def test_create_agenda_output():
    agenda = AgendaOutput(
        id=1,
    )
    assert agenda.id == 1

def test_create_agenda_day_hour():
    agenda_day_hour = AgendaDayHour(
        agenda_id=1,
        start_datetime=datetime.strptime("2021-10-22 00:00:00", "%Y-%m-%d %H:%M:%S"),
        end_datetime=datetime.strptime("2021-10-22 00:00:00", "%Y-%m-%d %H:%M:%S")
    )

    assert agenda_day_hour.start_datetime == datetime.strptime("2021-10-22 00:00:00", "%Y-%m-%d %H:%M:%S")
    assert agenda_day_hour.end_datetime == datetime.strptime("2021-10-22 00:00:00", "%Y-%m-%d %H:%M:%S")