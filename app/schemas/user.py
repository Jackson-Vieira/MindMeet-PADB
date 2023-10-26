import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    full_name: str
    city: str

class User(UserBase):
    id: int
    data_joined: datetime.datetime

class UserCreate(UserBase):
    password_hash: str