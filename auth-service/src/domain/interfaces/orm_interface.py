from abc import ABC, abstractmethod
from typing import Any, Generator, TypeVar, Generic

Entity = TypeVar("Entity")


# pylint: disable=missing-function-docstring
class ORMInterface(ABC, Generic[Entity]):
    """
    ORM Interface.

    This class defines the interface for any
    ORM (Object-Relational Mapping) implementation
    in the application. Classes implementing this
    interface must provide the logic to initialize
    and connect a specific ORM."
    """

    @abstractmethod
    def __init__(self) -> None:
        self.db_url = ""
        self.engine = None
        self.SessionLocal = None

    @abstractmethod
    def connect(self) -> Generator: ...

    @abstractmethod
    def execute(self, statement: Any) -> Any: ...

    @abstractmethod
    def save(self, entity: Entity) -> Entity: ...
