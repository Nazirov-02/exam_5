import bcrypt
from typing import Optional
from session import Session

session = Session()


def hash_password(raw_password: str | None):
    assert raw_password, 'Raw password can not be None'
    return bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def match_password(raw_password, encoded_password):
    assert raw_password, 'Raw password can not be None'
    assert encoded_password, 'Encoded password can not be None'
    return bcrypt.checkpw(raw_password.encode('utf-8'), encoded_password.encode('utf-8'))


class Response:
    def __init__(self,
                 status_code: int = 200,
                 message: Optional[str] = None):
        self.status_code = status_code
        self.message = message


class BadRequest:
    def __init__(self, status_code: int = 404, message: Optional[str] = None):
        self.status_code = status_code
        self.message = message


def login_required(func):
    def wrapper(*args, **kwargs):
        if not session.session:
            raise Exception("Login required")
        result = func(*args, **kwargs)
        return result

    return wrapper
