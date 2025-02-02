from injector import inject

from src.domain.dtos import StoreMessageDTO
from src.domain.entities import Message
from src.domain.interfaces import MessageRepositoryInterface


class StoreMessageService:
    """Store Message Service."""

    @inject
    def __init__(self, message_repository: MessageRepositoryInterface) -> None:
        self.message_repository = message_repository

    def execute(self, dto: StoreMessageDTO) -> Message:
        """Store a message in database."""
        data = dto.data
        entity = Message(**data)
        message = self.message_repository.create(entity=entity)
        return message
