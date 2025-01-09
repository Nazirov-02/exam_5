from db import cur
from models import User
from session import Session
from utils import login_required

session = Session()

def check_phone(phone):
    if len(phone) != 13:
        return False
    elif not phone.startswith('+998'):
        return False
    elif phone[4:6] not in ['90','91','94','99','88','97','98','33','50','95','94','93']:
        return False
    elif not  phone[6::].isalnum():
        return False
    return True

# if check_phone('+99851412720'):
#     print('ok')
# else:
#     print('no')

@login_required
def find_users_id():
    data : User | None = session.check_session()
    if not data:
        print("data yoq")
    query = '''SELECT id FROM users where phone_number = %s ;'''
    phone_number = (data.phone_number,)
    cur.execute(query,phone_number)
    user_id = cur.fetchone()
    assert user_id, 'User id not found'
    return user_id


def return_users_phone():
    data: User | None = session.check_session()
    print(data.phone_number)
    return data.phone_number