from datetime import datetime
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    """User entity."""

    id: int | None = Field(default=None, primary_key=True)
    email: str
    first_name: str
    last_name: str
    password: str
    created: datetime | None = None
    updated: datetime | None = None
