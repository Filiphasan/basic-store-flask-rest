from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    pass


def identity(payload):
    user_id = payload['identity']
    pass