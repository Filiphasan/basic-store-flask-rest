from flask_restful import Resource, reqparse
from db import db
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field cannot blank.')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field cannot be blank.')

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {'message':'A user with that username already exist!'}, 400
        user = UserModel(username = data['username'],password= data['password'])
        user.save_to_db()
        return user