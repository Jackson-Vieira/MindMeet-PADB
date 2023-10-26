import datetime

from pydantic import BaseModel

"""
# id SERIAL PRIMARY KEY,
# agenda_day_hour_id INTEGER NOT NULL,
# status VARCHAR(50) NOT NULL,
# reason VARCHAR(50) NOT NULL,
# anonymous BIT NOT NULL,
# created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
# FOREIGN KEY (agenda_day_hour_id) REFERENCES agenda_day_hour (id)
"""

class Appointment(BaseModel):
    status: bool
    reason: str
    anonymous: bool
    psychologist_id: int
    patient_id: int

class AppointmentCreate(Appointment):
    agenda_day_hour_id: int
    updated_at: str | None = None

class AppointmentOutput(Appointment):
    id: int
    agenda_day_hour_id: int
    created_at: str
    updated_at: str

class AppointmentRequest(BaseModel):
    agenda_day_hour_id: int
    reason: str
    status: bool

class AppointmentRequestCreate(AppointmentRequest):
    pass

class AppointmentRequestOutput(AppointmentRequest):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime