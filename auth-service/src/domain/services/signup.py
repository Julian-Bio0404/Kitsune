from injector import inject

from src.domain.dtos import SignUpDTO
from src.domain.entities import User
from src.domain.interfaces import UserRepositoryInterface


class SignUpService:
    """SignUp Service."""

    @inject
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.user_repository = user_repository

    def execute(self, dto: SignUpDTO) -> User:
        """
        Validate user by email and
        username, create it if it does not exist.
        """
        email = dto.email

        if self.user_repository.filter(User.email == email):
            raise ValueError(f"User with email '{email}' already exists")

        data = dto.data
        entity = User(**data)
        user = self.user_repository.create(entity=entity)
        return user
