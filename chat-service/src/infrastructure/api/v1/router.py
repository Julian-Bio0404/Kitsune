from fastapi import APIRouter

from src.infrastructure.api.v1.controllers import messages


v1_router = APIRouter()
messages_router = APIRouter()

messages_router.include_router(router=messages.router, prefix="/channels", tags=["messages"])

v1_router.include_router(router=messages_router, prefix="/chat", tags=["chat"])
