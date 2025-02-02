from datetime import datetime, timedelta

import jwt

from conf.settings import settings


def generate_token(
    data: dict,
    expires_in: int = settings.token_lifetime,
) -> str:
    """Generate a token according to th secret with HS256 algorithm."""
    payload = {
        **data,
        "exp": datetime.now() + timedelta(seconds=expires_in),
    }
    token = jwt.encode(payload, settings.secret, algorithm="HS256")
    return token


def decode_token(token: str) -> dict:
    """Decode a token with HS256 algorithm"""
    try:
        payload = jwt.decode(token, settings.secret, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError as exc:
        raise ValueError("Token has expired") from exc
    except jwt.InvalidTokenError as exc:
        raise ValueError("Invalid token") from exc
