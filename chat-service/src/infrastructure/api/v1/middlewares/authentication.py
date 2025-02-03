from starlette.authentication import (
    AuthCredentials,
    AuthenticationBackend,
    AuthenticationError,
)
from starlette.requests import HTTPConnection

from src.infrastructure.services import AuthenticationService


class WebsocketAuthenticationMiddleware(AuthenticationBackend):
    """Custom Authentication middleware to websocket."""

    async def authenticate(self, conn: HTTPConnection) -> tuple[AuthCredentials, dict]:
        """
        Implement authentication with the
        authentication microservice according to the token.
        """
        authorization = conn.headers.get("authorization")

        token = authorization.split(" ")[1] if authorization else None
        service = AuthenticationService()
        response, status, success = service.authenticate(token=token)

        if not success:
            response["status"] = status
            raise AuthenticationError(response)

        return AuthCredentials(["authenticated"]), response
