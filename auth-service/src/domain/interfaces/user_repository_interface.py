from abc import ABC

from src.domain.interfaces.repository_interface import RepositoryInterface


class UserRepositoryInterface(RepositoryInterface, ABC):
    """
    User Repository Interface.

    Inherit from RepositoryInterface,
    implement this class for a User repository.
    """
