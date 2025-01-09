from datetime import datetime

from models import User, UserRole
from session import Session
from utils import BadRequest, match_password, Response, hash_password, login_required
from db import cur,conn

session = Session()

def log_or_reg(phone_number:str,password:str):
    user: User | None = session.check_session()
    if user:
        return BadRequest(message="You already logged in.")

    get_user_by_phone_query = '''select * from users where phone_number = %s;'''
    data = (phone_number,)
    cur.execute(get_user_by_phone_query, data)
    user_data = cur.fetchone()
    if not user_data:
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        query = """INSERT INTO users(phone_number,password,first_name,last_name,login_try_count,role)
                   VALUES(%s,%s,%s,%s,%s,%s);"""
        data = (phone_number,hash_password(password),first_name,last_name,0,UserRole.USER.value)
        cur.execute(query,data)
        conn.commit()
        user: User = User.from_tuple(data)
        session.add_session(user)
        return Response(message="Login successfully")

    user: User = User.from_tuple(user_data)
    if not match_password(password, user.password):
        user_update_query = '''update users set login_try_count = login_try_count + 1 where username = %s;'''
        data = (user.phone_number,)
        cur.execute(user_update_query, data)
        return BadRequest(message="Username or Password Invalid")
    session.add_session(user)
    return Response(message="Login Successful")


def log_out():
       if session.session:
           session.session = None
           return Response(message='Logged out !')
       return BadRequest(message='You are not log in yet !')

