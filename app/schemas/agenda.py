import datetime

from pydantic import BaseModel


class Agenda(BaseModel):
    pass
class AgendaOutput(Agenda):
    id: int
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime

class AgendaDayHour(BaseModel):
    start_date_time: datetime.datetime
    end_date_time: datetime.datetime

class AgendaDayHourOutput(AgendaDayHour):
    id: int
    agenda_id: int