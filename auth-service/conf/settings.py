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
    secret: str
    token_lifetime: int

    class Config:
        """Config options."""

        env_file = str(Path(__file__).parent.parent / ".env")


@lru_cache()
def get_settings() -> Settings:
    """Return a singleton instance of Setting class."""
    return Settings()


settings = get_settings()
