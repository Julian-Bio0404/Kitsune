from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/")
def auth() -> JSONResponse:
    """
    Auth endpoint.
    Return the user data according to token.
    """
    data = {"message": "Hello world!"}
    content = jsonable_encoder(data)
    return JSONResponse(content=content, status_code=status.HTTP_200_OK)
