from abc import ABC, abstractmethod
from typing import Iterable, TypeVar
from uuid import UUID

from src.domain.interfaces.repository_interface import RepositoryInterface

Entity = TypeVar("Entity")


# pylint: disable=missing-function-docstring
class MessageRepositoryInterface(RepositoryInterface, ABC):
    """
    Message Repository Interface.

    Inherit from RepositoryInterface,
    implement this class for a Message repository.
    """

    @abstractmethod
    def filter_by_sender_and_receiver(
        self,
        sender_id: UUID,
        receiver_id: UUID,
    ) -> Iterable[Entity]: ...
