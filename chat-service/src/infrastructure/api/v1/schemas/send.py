from typing import Any

from pydantic import BaseModel


class SendMessageSchema(BaseModel):
    """Send Message schema."""

    text: str

    @property
    def data(self) -> dict[str, Any]:
        """Return attributes as a dict."""
        return self.model_dump()
