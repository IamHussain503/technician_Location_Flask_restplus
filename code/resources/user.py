import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('mobNum', type=str, required=True,
                        help='this field can not be left blank')
    parser.add_argument('password', type=str, required=True,
                        help='this field can not be left blank')

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['mobNum']):
            return {"message": " A user with this name already exist"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "user created"}


class UsersList(Resource):
    # @jwt_required()
    def get(self):
        return {'users': [x.json() for x in UserModel.query.all()]}


class UserById(Resource):
    # @jwt_required()
    def get(self, userId):
        user = UserModel.find_by_id(userId)
        if user:
            return user.json()
        return {'message': 'user not found'}, 404


class UserByMobile(Resource):
    def get(self, _mobNum):
        user = UserModel.find_by_mobile(_mobNum).first()
        if user:
            return user.json()
        return{'message': 'user not found'}, 404
