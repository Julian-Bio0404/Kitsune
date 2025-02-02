from fastapi import FastAPI

from src.infrastructure.api import router


app = FastAPI()
app.include_router(router=router.api_router, prefix="/api")
