from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Settings singleton class."""

    # ----- Postgres ----- #
    postgres_db: str = None
    postgres_user: str = None
    postgres_password: str = None
    postgres_host: str = None
    postgres_port: str = None
    postgres_url: str = (
        f"postgresql://{postgres_user}:"
        f"{postgres_password}@"
        f"{postgres_host}/"
        f"{postgres_db}"
    )

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
