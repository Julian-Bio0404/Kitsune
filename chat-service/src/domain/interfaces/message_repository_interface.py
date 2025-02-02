from abc import ABC

from src.domain.interfaces.repository_interface import RepositoryInterface


class MessageRepositoryInterface(RepositoryInterface, ABC):
    """
    Message Repository Interface.

    Inherit from RepositoryInterface,
    implement this class for a Message repository.
    """
