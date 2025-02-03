from typing import Any, Iterable
from uuid import UUID

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

    async def filter(self, expression: Any) -> Iterable[Message]:
        """Filter messages by statement."""
        messages = await self.odm.filter(entity=Message, statement=expression)
        return messages.to_list()

    async def filter_by_sender_and_receiver(
        self,
        sender_id: UUID,
        receiver_id: UUID,
    ):
        """Filter messages by sender and receiver."""
        expression = {
            "$and": [
                {"sender_id": {"$in": [sender_id, receiver_id]}},
                {"receiver_id": {"$in": [sender_id, receiver_id]}}
            ]
        }
        messages = await self.odm.filter(entity=Message, statement=expression)
        return messages.to_list()
