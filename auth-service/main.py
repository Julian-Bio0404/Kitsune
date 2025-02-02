from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
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


# TODO: Create custom exceptions
@app.exception_handler(ValueError)
async def exception_handler(_: Request, exc: ValueError):
    """Handle API exceptions."""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": str(exc)}
    )
