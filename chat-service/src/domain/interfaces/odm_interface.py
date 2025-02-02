from abc import ABC, abstractmethod
from typing import Any, Generator, TypeVar, Generic

Entity = TypeVar("Entity")


# pylint: disable=missing-function-docstring
class ODMInterface(ABC, Generic[Entity]):
    """
    ODM Interface.

    This class defines the interface for any
    ODM (Object-Relational Mapping) implementation
    in the application. Classes implementing this
    interface must provide the logic to initialize
    and connect a specific ODM."
    """

    @abstractmethod
    def __init__(self) -> None:
        self.db_url = ""
        self.engine = None

    @abstractmethod
    def connect(self) -> Generator: ...

    @abstractmethod
    def execute(self, statement: Any) -> Any: ...

    @abstractmethod
    def save(self, entity: Entity) -> Entity: ...
