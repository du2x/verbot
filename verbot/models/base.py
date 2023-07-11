from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func


class SimpleIdBaseModel(SQLModel):
    """Base Model with autoincremented integer id"""
    id: Optional[int] = Field(default=None, primary_key=True)


class TimeTrackedBaseModel(SimpleIdBaseModel):
    """Base Model with autoincremented integer id and time tracking fields"""

    time_created: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )
    time_updated: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), onupdate=func.now())
    )
