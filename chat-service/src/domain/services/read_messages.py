from injector import inject

from src.domain.dtos import ReadMessageDTO
from src.domain.entities import Message
from src.domain.interfaces import MessageRepositoryInterface


class ReadMessageService:
    """Read Message Service."""

    @inject
    def __init__(self, message_repository: MessageRepositoryInterface) -> None:
        self.message_repository = message_repository

    async def execute(self, dto: ReadMessageDTO) -> list[Message]:
        """Get messages."""
        messages = await self.message_repository.filter_by_sender_and_receiver(
            sender_id=dto.sender_id,
            receiver_id=dto.receiver_id,
        )
        return await messages
