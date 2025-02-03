from typing import Any
from uuid import UUID

from pydantic import BaseModel


class ReadMessageDTO(BaseModel):
    """Read Message DTO."""

    sender_id: UUID
    receiver_id: UUID

    @property
    def data(self) -> dict[str, Any]:
        """Return attributes as a dict."""
        return self.model_dump()
