# to compare different encoding strings safelya nd securely
from werkzeug.security import safe_str_cmp
from models.user import UserModel
import sqlite3


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):

        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
