from abc import ABC, abstractmethod
from typing import Any, Iterable, TypeVar

Entity = TypeVar("Entity")


# pylint: disable=missing-function-docstring
class RepositoryInterface(ABC):
    """Repository interface."""

    @abstractmethod
    def create(self, entity: Entity) -> Entity: ...

    @abstractmethod
    def update(self, entity: Entity) -> Entity: ...

    @abstractmethod
    def filter(self, expression: Any) -> Iterable[Entity]: ...
