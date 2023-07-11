from fastapi import APIRouter
from typing import Optional, List
from sqlmodel import select, Session
from verbot.models.chat import Chat, ChatResponse, ChatRequest
from verbot.db import ActiveSession

router = APIRouter()


@router.get("/user/{id}/chats", response_model=List[ChatResponse])
async def list_chats(id: int, *, session: Session = ActiveSession) -> List[Chat]:
    return session.exec(select(Chat).where(Chat.user_id == id)).all()
