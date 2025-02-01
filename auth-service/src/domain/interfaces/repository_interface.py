from abc import ABC, abstractmethod
from typing import Any, Iterable, TypeVar

# from src.domain.entities.abstract_entity import Entity

Entity = TypeVar("Entity")


# pylint: disable=missing-function-docstring
class RepositoryInterface(ABC):
    """Repository interface."""

    @abstractmethod
    def create(self, entity: Entity) -> Entity: ...

    @abstractmethod
    def update(self, entity: Entity) -> Entity: ...

    @abstractmethod
    def delete(self, entity: Entity) -> None: ...

    @abstractmethod
    def bulk_create(self, entities: Iterable[Entity]) -> Iterable[Entity]: ...

    @abstractmethod
    def bulk_update(self, entities: Iterable[Entity]) -> Iterable[Entity]: ...

    @abstractmethod
    def bulk_delete(self, entities: Iterable[Entity]) -> None: ...

    @abstractmethod
    def filter(self, statement: Any) -> Iterable[Entity]: ...
