from fastapi import APIRouter

from src.infrastructure.api.v1.controllers import auth


v1_router = APIRouter()
v1_router.include_router(router=auth.router, prefix="/auth", tags=["auth"])
