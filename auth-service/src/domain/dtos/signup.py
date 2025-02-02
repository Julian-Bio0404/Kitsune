from typing import Any
from pydantic import BaseModel, EmailStr


class SignUpDTO(BaseModel):
    """SignUp DTO."""

    first_name: str
    last_name: str
    email: EmailStr
    password: str

    @property
    def data(self) -> dict[str, Any]:
        """Return attributes as a dict."""
        return self.model_dump()
