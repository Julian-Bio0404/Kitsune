from datetime import datetime
from fastapi import APIRouter, WebSocket

from src.dependencies import create_object
from src.domain.dtos import StoreMessageDTO
from src.domain.services import StoreMessageService
from src.infrastructure.api.v1.schemas import SendMessageSchema

router = APIRouter()


@router.websocket("/{id}/")
async def messages(
    websocket: WebSocket,
    id: str,
):
    """Send or get messages user <-> user."""
    await websocket.accept()

    while True:
        data: dict = await websocket.receive_json(),
        schema = SendMessageSchema(**data[0])

        dto = StoreMessageDTO(
            sender_id="b84e4b39-50f1-4a2b-a86b-68b9123fdc96",
            receiver_id=id,
            text=schema.text,
            created=datetime.now(),
            updated=datetime.now(),
        )

        service = create_object(StoreMessageService)
        await service.execute(dto=dto)
        await websocket.send_json(data)
