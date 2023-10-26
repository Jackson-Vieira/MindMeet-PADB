import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    full_name: str
    city: str


class User(UserBase):
    id: str
    data_joined: datetime.datetime
