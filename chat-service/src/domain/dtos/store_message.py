from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel


class StoreMessageDTO(BaseModel):
    """Store Message DTO."""

    sender_id: UUID
    receive_id: UUID
    text: str
    created: datetime
    updated: datetime

    @property
    def data(self) -> dict[str, Any]:
        """Return attributes as a dict."""
        return self.model_dump()
