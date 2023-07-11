from typing import Optional, List
from fastapi import FastAPI
from sqlmodel import select, Session
from starlette.status import HTTP_404_NOT_FOUND
from verbot.db import ActiveSession
from verbot.models.user import User, UserResponse
from verbot.models.chat import Chat, ChatResponse


app = FastAPI(
    title="verbot API",
    version="0.1.0",
    description="API para o verbot",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users/{id}", response_model=UserResponse)
async def user_detail(id: int, *, session: Session = ActiveSession) -> Optional[User]:
    user = session.exec(select(User).where(User.id == id)).first()
    if user:
        return user
    else:
        return None


@app.get("/user/{id}/chats", response_model=List[ChatResponse])
async def list_chats(id: int, *, session: Session = ActiveSession) -> List[Chat]:
    return session.exec(select(Chat).where(Chat.user_id == id)).all()
