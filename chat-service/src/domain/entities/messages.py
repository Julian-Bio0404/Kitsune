from datetime import datetime
from typing import Any
from uuid import UUID, uuid4

from beanie import Document
from pydantic import Field


class Message(Document):
    """Message entity."""

    id: UUID = Field(default_factory=uuid4)
    sender_id: UUID
    receiver_id: UUID
    text: str
    created: datetime = Field(default_factory=datetime.now)
    updated: datetime = Field(default_factory=datetime.now)

    class Settings:
        """Setting options."""
        name = "messages"

    @property
    def data(self) -> dict[str, Any]:
        """Return attributes as dict"""
        return self.model_dump()
