from pydantic import BaseModel


class Agenda(BaseModel):
    pass

class AgendaCreate(Agenda):
    psychologist_id: int
    
class AgendaDayHour(BaseModel):
    start_datetime: str
    end_datetime: str
    # available: bool

class AgendaOutput(Agenda):
    id: int
    psychologist_id: int
    available_days: list[AgendaDayHour]

class AgendaDayHourCreate(AgendaDayHour):
    agenda_id: int
    psychologist_id: int
