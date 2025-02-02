from contextlib import contextmanager
from typing import Any, Generator, TypeVar

from sqlalchemy import Sequence
from sqlalchemy.engine import Row
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
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def execute(self, statement: Any) -> Sequence[Row[Any]]:
        """Execute a SQL statement and return the results."""
        with self.connect() as session:
            session: Session
            result = session.exec(statement=statement)
            return result

    def insert(self, entity: Entity) -> Entity:
        """Insert a entity in database."""
        with self.connect() as session:
            session: Session
            session.add(entity)
        return entity

    def update(self, entity: Entity) -> Entity:
        """Update a entity from database."""
        with self.connect() as session:
            session: Session
            session.add(entity)
            session.refresh(entity)

        return entity
