from injector import inject

from src.domain.dtos import LoginDTO
from src.domain.entities import User
from src.domain.interfaces import UserRepositoryInterface


class LoginService:
    """Login Service."""

    @inject
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    def execute(self, dto: LoginDTO) -> User:
        """Return a user by email."""
        user = self.user_repository.get(User.email == dto.email)
        return user
