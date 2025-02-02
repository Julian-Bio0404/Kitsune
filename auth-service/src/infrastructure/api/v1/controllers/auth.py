from fastapi import APIRouter, Header, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src import dependencies
from src.domain.entities import User
from src.domain.interfaces import UserRepositoryInterface
from src.infrastructure.api.v1.schemas import UserSchema
from src.infrastructure.api.v1.utils.jwt import decode_token

router = APIRouter()


@router.get("/")
def auth(authorization: str = Header(...)) -> JSONResponse:
    """
    Authentication endpoint.
    Return the user data according to token.
    """
    if not authorization:
        content = jsonable_encoder({"detail": "Authorization header missing"})
        return JSONResponse(content=content, status_code=status.HTTP_401_UNAUTHORIZED)

    token = authorization.split(" ")[1]
    payload = decode_token(token=token)
    user_id = payload["id"]

    repository = dependencies.get(UserRepositoryInterface)
    user: User = repository.get(User.id == user_id)

    data = UserSchema(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        created=user.created,
        updated=user.updated,
    ).data

    content = jsonable_encoder(data)
    return JSONResponse(content=content, status_code=status.HTTP_200_OK)
