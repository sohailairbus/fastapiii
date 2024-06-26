

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True

        
