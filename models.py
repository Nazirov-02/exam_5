from datetime import datetime
from enum import Enum

class UserRole(Enum):
    ADMIN = 'admin'
    USER = 'user'


class User:
    def __init__(self,phone_number:str ,password:str,first_name:str,
                 last_name:str,role:str | None = None,user_id:str | None = None,login_try_count:int |None = None,created_at : datetime| None = None):
        self.phone_number = phone_number
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = user_id
        self.login_try_count = login_try_count or 0
        self.role = role or UserRole.USER.value
        self.created_at = created_at

    @staticmethod
    def from_tuple(args):
        return User(
            user_id = args[0],
            phone_number = args[1],
            password = args[2],
            first_name = args[3],
            last_name = args[4],
            login_try_count = args[5]
            )



