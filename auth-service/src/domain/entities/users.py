from typing import Any
from uuid import UUID, uuid4
from datetime import datetime

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    """User entity."""

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: str
    first_name: str
    last_name: str
    password: str
    created: datetime = Field(default_factory=datetime.now)
    updated: datetime = Field(default_factory=datetime.now)

    @property
    def data(self) -> dict[str, Any]:
        """Return attributes as a dict."""
        return self.model_dump()
