from datetime import datetime
from uuid import UUID, uuid4

from beanie import Document
from pydantic import Field


class Message(Document):
    """Message entity."""

    id: UUID = Field(default_factory=uuid4)
    sender_id: UUID
    receiver_id: UUID
    text: str
    created: datetime
    updated: datetime

    class Settings:
        """Setting options."""
        name = "messages"
