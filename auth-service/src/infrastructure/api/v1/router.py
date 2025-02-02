from fastapi import APIRouter

from src.infrastructure.api.v1.controllers import auth, signup, login


v1_router = APIRouter()

v1_router.include_router(router=auth.router, prefix="/auth", tags=["auth"])
v1_router.include_router(router=signup.router, prefix="/signup", tags=["signup"])
v1_router.include_router(router=login.router, prefix="/login", tags=["signup"])
