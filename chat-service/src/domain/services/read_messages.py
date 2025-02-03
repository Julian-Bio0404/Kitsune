from injector import inject

from src.domain.dtos import StoreMessageDTO
from src.domain.entities import Message
from src.domain.interfaces import MessageRepositoryInterface


class ReadMessageService:
    """Read Message Service."""

    @inject
    def __init__(self, message_repository: MessageRepositoryInterface) -> None:
        self.message_repository = message_repository

    async def execute(self) -> list[Message]:
        """Get messages."""
        messages = await self.message_repository.filter(
            entity=Message,
            expression={},
        )
        return await messages
