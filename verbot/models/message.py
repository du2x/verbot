"""Message related data models"""
from typing import Optional
from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey
from sqlmodel import Field
from pydantic import BaseModel
from .base import TimeTrackedBaseModel


class Message(TimeTrackedBaseModel, table=True):
    """Represents the Chat Model"""

    content: str = Field(default="Nova conversa")
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    chat_id: Optional[int] = Field(default=None, foreign_key="chat.id")


class MessageResponse(BaseModel):
    """Represents the Message Response Model"""
    id: int
    user_id: Optional[int]
    chat_id: int
    content: str
    time_created: datetime
    time_updated: Optional[datetime]


class MessageRequest(BaseModel):
    """Represents the Message Request Model"""
    id: Optional[int]
    user_id: int
    chat_id: int
    content: str
