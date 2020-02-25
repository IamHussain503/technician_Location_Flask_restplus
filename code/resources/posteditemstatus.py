from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from models.posteditemstatus import PostedItemStatusModel


class PostedItemStatus(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('status', type=str, required=True,
                        help='subskill Detail is mandatory')

    #
    # @jwt_required()

    def put(self, _id):
        data = PostedItemStatus.parser.parse_args()
        posteditemstatus = PostedItemStatusModel.find_by_id(_id)
        posteditemstatus.status = data['status']

        posteditemstatus.save_to_db()
        return posteditemstatus.json()
