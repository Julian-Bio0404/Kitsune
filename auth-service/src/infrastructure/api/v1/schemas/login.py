from typing import Any

from pydantic import BaseModel, EmailStr


class UserLoginSchema(BaseModel):
    """User login schema."""

    email: EmailStr
    password: str

    @property
    def data(self) -> dict[str, Any]:
        """Return attributes as a dict."""
        return self.model_dump()
