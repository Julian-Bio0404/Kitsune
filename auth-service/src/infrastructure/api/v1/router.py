from fastapi import APIRouter

from src.infrastructure.api.v1.controllers import auth, signup, login


v1_router = APIRouter()
auth_router = APIRouter()

auth_router.include_router(router=auth.router, prefix="", tags=["auth"])
auth_router.include_router(router=signup.router, prefix="/signup", tags=["signup"])
auth_router.include_router(router=login.router, prefix="/login", tags=["login"])

v1_router.include_router(router=auth_router, prefix="/auth", tags=["auth"])
