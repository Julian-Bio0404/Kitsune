from typing import Any
from pydantic import BaseModel


class LoginDTO(BaseModel):
    """Login DTO."""

    email: str
    password: str

    @property
    def data(self) -> dict[str, Any]:
        """Return attributes as a dict."""
        return self.model_dump()
