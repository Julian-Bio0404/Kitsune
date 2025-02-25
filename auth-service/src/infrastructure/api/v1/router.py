from fastapi import APIRouter

from src.infrastructure.api.v1.controllers import auth, signup, login


v1_router = APIRouter(prefix="/v1")
auth_router = APIRouter(prefix="/auth")

auth_router.include_router(router=auth.router, prefix="")
auth_router.include_router(router=signup.router, prefix="/signup")
auth_router.include_router(router=login.router, prefix="/login")

v1_router.include_router(router=auth_router, tags=["auth"])
