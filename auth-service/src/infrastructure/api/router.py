from fastapi import APIRouter

from src.infrastructure.api.v1.router import v1_router

# ---------------------------- V1 routers ----------------------------
api_router = APIRouter(prefix="/api")
api_router.include_router(router=v1_router)
