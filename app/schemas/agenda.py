import datetime

from pydantic import BaseModel


class Agenda(BaseModel):
    pass
class AgendaOutput(Agenda):
    id: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime
class AgendaDayHour(BaseModel):
    agenda_id: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime