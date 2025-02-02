from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel


class UserSchema(BaseModel):
    """User schema."""

    id: UUID
    first_name: str
    last_name: str
    email: str
    created: datetime
    updated: datetime

    @property
    def data(self) -> dict[str, Any]:
        """Return attributes as a dict."""
        return self.model_dump()
