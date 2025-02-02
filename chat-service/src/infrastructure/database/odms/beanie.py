from typing import Any, TypeVar

from motor.motor_asyncio import AsyncIOMotorClient
from beanie import Document, init_beanie

from conf.settings import MONGO_URL
from src.domain.interfaces import ODMInterface


Entity = TypeVar("Entity")


class BeanieODM(ODMInterface[Entity]):
    """Beanie ODM implementation."""

    def __init__(self) -> None:
        self.db_url = MONGO_URL
        self.engine = AsyncIOMotorClient(self.db_url)

    async def connect(self, document_models: list[Entity]) -> None:
        """Init beanie ODM with the document models."""
        await init_beanie(database=self.engine.db_name, document_models=document_models)

    async def create(self, entity: Document) -> Entity:
        """Insert a entity in database."""
        await entity.create()

    async def update(self, entity: Document) -> Entity:
        """Update a entity in database."""
        await entity.save()

    async def filter(self, entity: Document, statement: Any):
        """Execute a NO-SQL statement and return the results."""
        await entity.find(statement)
