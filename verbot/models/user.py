"""User related data models"""
from typing import Optional
from sqlmodel import Field
from pydantic import BaseModel
from .base import TimeTrackedBaseModel


class User(TimeTrackedBaseModel, table=True):
    """Represents the User Model"""

    email: str = Field(unique=True, nullable=False)
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserResponse(BaseModel):
    """Represents the User Response Model"""
    id: int
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserRequest(BaseModel):
    """Represents the User Request Model"""
    id: Optional[int]
    email: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
