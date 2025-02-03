from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings singleton class."""

    # ----- MongoDB ----- #
    mongo_initdb_root_username: str
    mongo_initdb_root_password: str
    mongo_host: str
    mongo_port: str

    # ----- Authentication service ----- #
    authentication_service_url: str

    class Config:
        """Config options."""

        env_file = str(Path(__file__).parent.parent / ".env")


@lru_cache()
def get_settings() -> Settings:
    """Return a singleton instance of Setting class."""
    return Settings()


settings = get_settings()

MONGO_URL = (
    f"mongodb://{settings.mongo_initdb_root_username}:"
    f"{settings.mongo_initdb_root_password}@"
    f"{settings.mongo_host}:"
    f"{settings.mongo_port}"
)
