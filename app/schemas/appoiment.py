from pydantic import BaseModel


class Appoiment(BaseModel):
    status: bool
    description: str
    reason: str
    anonymous: bool

class AppoimentCreate(Appoiment):
    agenda_day_hour_id: int
    psychologist_id: int
    patient_id: int

class AppoimentOutput(Appoiment):
    id: int
    agenda_day_hour_id: int
    psychologist_id: int
    patient_id: int