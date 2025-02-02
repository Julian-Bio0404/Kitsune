from fastapi import APIRouter, WebSocket

router = APIRouter()


@router.websocket("/{id}/")
async def messages(
    websocket: WebSocket,
    id: str,
):
    """Send or get messages user <-> user."""
    await websocket.accept()
    while True:
        data = {
            "text": await websocket.receive_text(),
        }
        await websocket.send_json(data)
