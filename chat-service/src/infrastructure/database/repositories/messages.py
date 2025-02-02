from typing import Any, Iterable

from injector import inject

from src.domain.entities import Message
from src.domain.interfaces import MessageRepositoryInterface
from src.domain.interfaces import ODMInterface


class MessageRepository(MessageRepositoryInterface):
    """Message Repository implementation."""

    @inject
    def __init__(self, odm: ODMInterface) -> None:
        self.odm = odm

    async def create(self, entity: Message) -> Message:
        """Store a message in database."""
        message = await self.odm.create(entity=entity)
        return message

    async def update(self, entity: Message) -> Message:
        """Update a message in database."""
        message = await self.odm.update(entity=entity)
        return message

    async def filter(self, entity: Message, expression: Any) -> Iterable[Message]:
        """Filter messages by statement."""
        messages = await self.odm.filter(entity=entity, statement=expression)
        return messages.to_list()
