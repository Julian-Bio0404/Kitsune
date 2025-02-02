from typing import Any

from pydantic import BaseModel


class UserLoginSchema(BaseModel):
    """User login schema."""

    email: str
    password: str

    @property
    def data(self) -> dict[str, Any]:
        """Return attributes as a dict."""
        return self.model_dump()
