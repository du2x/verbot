"""Chat related data models"""
from typing import Optional
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey
from sqlmodel import Field
from pydantic import BaseModel
from .base import TimeTrackedBaseModel


class Chat(TimeTrackedBaseModel, table=True):
    """Represents the Chat Model"""

    title: str = Field(default="Nova conversa")
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")


class ChatResponse(BaseModel):
    """Represents the Chat Request Model"""

    id: int
    user_id: int
    title: str
    time_created: datetime
    time_updated: Optional[datetime]


class ChatRequest(BaseModel):
    """Represents the Chat Request Model"""
    id: Optional[int]
    user_id: int
