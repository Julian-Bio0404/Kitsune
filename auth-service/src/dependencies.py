from typing import TypeVar

from injector import Injector, SingletonScope

from src.domain.interfaces import ORMInterface, UserRepositoryInterface
from src.infrastructure.database.repositories import UserRepository
from src.infrastructure.database.orms import SQLModelORM


injector = Injector()

T = TypeVar("T")


def bind_dependencies() -> None:
    """
    Bind application dependencies to the injector.

    Binds various application interfaces to their respective implementations
    using the injector. The bindings are set up with a `SingletonScope`, ensuring
    that single instances of each implementation are shared across the application.

    This setup allows for dependency injection throughout the application, ensuring
    that the correct implementations are used where needed.
    """
    # ------- bind ORM dependencies -------
    injector.binder.bind(
        interface=ORMInterface,
        to=SQLModelORM,
        scope=SingletonScope,
    )

    # ------- bind User Service dependencies -------

    # Repositories
    injector.binder.bind(
        interface=UserRepositoryInterface,
        to=UserRepository,
        scope=SingletonScope,
    )


def get(interface: type[T]) -> T:
    """
    Retrieve an instance of the specified interface from the injector.

    Take an interface type as input and returns an instance of the bound
    implementation. The injector ensures that the correct dependencies are
    provided based on the bindings defined in `bind_dependencies`.
    """
    return injector.get(interface)


def create_object(cls: type[T]) -> T:
    """
    Create an instance of a class with dependencies injected.

    Create an instance of the given class, automatically
    injecting any dependencies required by the class's constructor.
    The injector resolves and provides the necessary dependencies.
    """
    return injector.create_object(cls)
