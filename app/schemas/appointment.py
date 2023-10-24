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

class Appoiment(BaseModel):
    status: bool
    reason: str
    anonymous: bool

class AppoimentCreate(Appoiment):
    agenda_day_hour_id: int
    # patient_id: int

class AppoimentOutput(Appoiment):
    id: int
    agenda_day_hour_id: int
    created_at: str
    updated_at: str
    # psychologist_id: int
    # patient_id: int

class AppoimentRequest(BaseModel):
    agenda_day_hour_id: int
    reason: str
    status: bool
    anonymous: bool