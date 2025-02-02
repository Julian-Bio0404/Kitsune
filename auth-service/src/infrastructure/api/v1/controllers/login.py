import bcrypt
from fastapi import APIRouter, Body, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.dependencies import create_object
from src.domain.dtos import LoginDTO
from src.domain.services import LoginService
from src.infrastructure.api.v1.schemas import UserLoginSchema, UserSchema
from src.infrastructure.api.v1.utils.jwt import generate_token

router = APIRouter()


@router.post("/")
def login(schema: UserLoginSchema = Body(...)) -> JSONResponse:
    """
    Login endpoint.
    Return the user data with auth token according to user credentials.
    """
    service = create_object(LoginService)
    user = service.execute(dto=LoginDTO(**schema.data))

    valid_password = bcrypt.checkpw(
        schema.password.encode("utf-8"),
        user.password.encode("utf-8"),
    )

    if not valid_password:
        content = jsonable_encoder({"detail": "Incorrect credentials"})
        return JSONResponse(content=content, status_code=status.HTTP_400_BAD_REQUEST)

    payload = {
        "id": str(user.id),
        "email": user.email,
    }

    token = generate_token(data=payload)

    data = {
        "user": UserSchema(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            created=user.created,
            updated=user.updated,
        ).data,
        "token": token,
    }

    content = jsonable_encoder(data)
    return JSONResponse(content=content, status_code=status.HTTP_200_OK)
