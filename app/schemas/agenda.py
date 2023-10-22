from pydantic import BaseModel


class Agenda(BaseModel):
    pass
class AgendaOutput(Agenda):
    id: int
class AgendaDayHour(BaseModel):
    agenda_id: int
    start_datetime: str
    end_datetime: str