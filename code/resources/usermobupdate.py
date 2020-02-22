from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from models.user import UserModel


class UserMobUpdate(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('mobNum', type=str, required=True,
                        help='WorkerId is mandatory')

    #
    # @jwt_required()

    def put(self, userId):
        data = UserMobUpdate.parser.parse_args()
        user = UserModel.find_by_id(userId)
        user.mobNum = data['mobNum']

        user.save_to_db()
        return user.json()
