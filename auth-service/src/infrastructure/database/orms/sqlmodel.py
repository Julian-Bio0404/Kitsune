from contextlib import contextmanager
from typing import Any, Generator, TypeVar

from sqlalchemy.engine.result import ScalarResult
from sqlmodel import Session, create_engine

from conf.settings import POSTGRES_URL
from src.domain.interfaces import ORMInterface


Entity = TypeVar("Entity")


class SQLModelORM(ORMInterface[Entity]):
    """SQLModel ORM implementation."""

    def __init__(self) -> None:
        self.db_url = POSTGRES_URL
        self.engine = create_engine(self.db_url)

    @contextmanager
    def connect(self) -> Generator[Session, None, None]:
        """
        Create a new session that is provided as a context
        manager, ensuring that it is properly closed after
        use, even if an error occurs.
        """
        session = Session(self.engine)
        try:
            yield session
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def execute(self, statement: Any) -> ScalarResult[Any]:
        """Execute a SQL statement and return the results."""
        with self.connect() as session:
            session: Session
            results = session.exec(statement=statement).all()
            return results

    def save(self, entity: Entity) -> Entity:
        """Insert or update a entity in database."""
        with self.connect() as session:
            session: Session
            session.add(entity)
            session.commit()
            session.refresh(entity)
        return entity
