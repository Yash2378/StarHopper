from pydantic import BaseModel, Field
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str
    user_type: str = Field(..., regex="^(pilot|passenger)$")

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    user_type: str

    class Config:
        orm_mode = True

class RideCreate(BaseModel):
    origin: str
    destination: str
    price: float

class RideOut(BaseModel):
    id: int
    origin: str
    destination: str
    price: float
    status: str
    passenger_id: int
    pilot_id: Optional[int]

    class Config:
        orm_mode = True
