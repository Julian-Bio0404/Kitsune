from fastapi import APIRouter

from src.infrastructure.api.v1.router import v1_router

# ---------------------------- V1 routers ----------------------------
api_router = APIRouter()
api_router.include_router(v1_router, prefix="/v1")
