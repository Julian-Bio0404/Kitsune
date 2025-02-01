from typing import Any, Iterable

from injector import inject
from sqlmodel import select

from src.domain.entities import User
from src.domain.interfaces import UserRepositoryInterface
from src.domain.interfaces import ORMInterface


class UserRepository(UserRepositoryInterface):
    """User Repository implementation."""

    @inject
    def __init__(self, orm: ORMInterface) -> None:
        self.orm = orm

    def create(self, entity: User) -> User:
        """Store a user in database."""
        user = self.orm.insert(entity=entity)
        return user

    def update(self, entity: User) -> User:
        """Update a user."""
        user = self.orm.update(entity=entity)
        return user

    def filter(self, expression: Any) -> Iterable[User]:
        """Filter users by statement."""
        statement = select(User).where(expression)
        users = self.orm.execute(statement=statement)
        return users

    def delete(self, entity: User) -> None:
        """Delete a user."""
        pass
