import bcrypt
from fastapi import APIRouter, Body, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from src.dependencies import create_object
from src.domain.dtos import SignUpDTO
from src.domain.services import SignUpService
from src.infrastructure.api.v1.schemas import UserSchema, UserSignUpSchema

router = APIRouter()


@router.post("/")
def signup(schema: UserSignUpSchema = Body(...)) -> JSONResponse:
    """
    Sign-up endpoint.
    Check password and create user.
    """
    # Hash password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(schema.password.encode("utf-8"), salt)
    schema.password = hashed_password.decode("utf-8")

    service = create_object(SignUpService)

    user = service.execute(dto=SignUpDTO(**schema.data))
    data = UserSchema(
        id=user.id,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        created=user.created,
        updated=user.updated
    )
    content = jsonable_encoder(data)
    return JSONResponse(content=content, status_code=status.HTTP_201_CREATED)
