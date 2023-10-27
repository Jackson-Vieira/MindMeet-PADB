from pydantic import BaseModel
import datetime

"""
# id SERIAL PRIMARY KEY,
# username VARCHAR(50) NOT NULL,
# email VARCHAR(100) NOT NULL,
# password VARCHAR(100) NOT NULL,
# created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
"""
    
class User(BaseModel):
    id: int
    username: str
    email: str
    city: str
    password: str
    created_at: datetime.datetime

class UserCreate(User):
    pass
