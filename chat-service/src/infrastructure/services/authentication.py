import requests

from conf.settings import settings


class AuthenticationService:
    """
    Authentication Service.

    Service class to authenticate a user to the
    authentication microservice based on the token
    """

    def __init__(self):
        self.service_url = settings.authentication_service_url

    def authenticate(self, token: str | None) -> tuple[dict, int, bool]:
        """
        Get user information associated
        with the authentication service token.
        """
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        response = requests.get(url=self.service_url, headers=headers)
        return response.json(), response.status_code, response.ok
