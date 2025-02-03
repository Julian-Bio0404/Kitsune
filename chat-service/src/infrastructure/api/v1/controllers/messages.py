from fastapi import APIRouter, WebSocket
from fastapi.encoders import jsonable_encoder

from src.dependencies import create_object
from src.domain.dtos import ReadMessageDTO, StoreMessageDTO
from src.domain.services import ReadMessageService, StoreMessageService
from src.infrastructure.api.v1.schemas import SendMessageSchema, MessageSchema

router = APIRouter()


@router.websocket("/{id}/")
async def messages(
    websocket: WebSocket,
    id: str,
):
    """Send or get messages user <-> user."""
    user = websocket.scope["user"]

    # Send previous messages
    service = create_object(cls=ReadMessageService)
    dto = ReadMessageDTO(
        sender_id=user["id"],
        receiver_id=id,
    )
    _messages = await service.execute(dto=dto)
    data = jsonable_encoder([MessageSchema(**m.data).data for m in _messages])

    await websocket.accept()
    await websocket.send_json(data=data)

    while True:
        # Get, Store and send new messages
        data: dict = await websocket.receive_json(),
        schema = SendMessageSchema(**data[0])

        dto = StoreMessageDTO(
            sender_id=user["id"],
            receiver_id=id,
            text=schema.text,
        )

        service = create_object(cls=StoreMessageService)
        message = await service.execute(dto=dto)
        data = jsonable_encoder(MessageSchema(**message.data).data)
        await websocket.send_json(data=data)
