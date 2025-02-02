from fastapi import FastAPI
from fastapi_injector import attach_injector

from src import dependencies
from src.infrastructure.api import router

app = FastAPI()

# Initialize dependency injection
dependencies.bind_dependencies()
attach_injector(app, dependencies.injector)

# Execute migrations
dependencies.migrate()

# Include default router
app.include_router(router=router.api_router, prefix="/api")
