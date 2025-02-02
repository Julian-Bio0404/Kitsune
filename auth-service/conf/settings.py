from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings singleton class."""

    # ----- Postgres ----- #
    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: str

    # ----- JWT ----- #
    secret: str = None
    token_lifetime: int = None

    class Config:
        """Config options."""

        env_file = str(Path(__file__).parent.parent / ".env")


@lru_cache()
def get_settings() -> Settings:
    """Return a singleton instance of Setting class."""
    return Settings()


settings = get_settings()

POSTGRES_URL = (
    f"postgresql://{settings.postgres_user}:"
    f"{settings.postgres_password}@"
    f"{settings.postgres_host}/"
    f"{settings.postgres_db}"
)
