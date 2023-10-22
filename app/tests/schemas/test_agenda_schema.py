from app.schemas.agenda import AgendaDayHour, AgendaOutput


def test_create_agenda_output():
    agenda = AgendaOutput(
        id=1,
    )
    assert agenda.id == 1

def test_create_agenda_day_hour():
    agenda_day_hour = AgendaDayHour(
        agenda_id=1,
        start_datetime="2021-10-22 00:00:00",
        end_datetime="2021-10-22 00:00:00",
    )

    assert agenda_day_hour.start_datetime == "2021-10-22 00:00:00"
    assert agenda_day_hour.end_datetime == "2021-10-22 00:00:00"