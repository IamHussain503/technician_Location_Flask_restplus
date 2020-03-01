from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from models.qoutestate import QouteStateModel


class QouteState(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('state', type=str, required=True,
                        help='WorkerId is mandatory')

    # @jwt_required()

    def get(self, _id):
        data = TaskStatus.parser.parse_args()
        taskstatus = QouteStatusModel.find_by_id(_id)
        taskstatus.statusName = data['statusName']

        taskstatus.save_to_db()
        return taskstatus.json()
