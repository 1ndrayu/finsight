from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    name: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class ProposalBase(BaseModel):
    title: str
    description: str
    location: str = ""

class ProposalCreate(ProposalBase):
    user_id: int

class Proposal(ProposalBase):
    id: int
    timestamp: datetime
    user: User

    class Config:
        orm_mode = True
