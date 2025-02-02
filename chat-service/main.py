from fastapi import FastAPI
from fastapi_injector import attach_injector

from src import dependencies
from src.infrastructure.api import router


async def lifespan(app: FastAPI):
    """Execute migrations."""
    await dependencies.migrate()
    yield


app = FastAPI(lifespan=lifespan)

# Initialize dependency injection
dependencies.bind_dependencies()
attach_injector(app, dependencies.injector)

# Include default router
app.include_router(router=router.api_router, prefix="/api")
