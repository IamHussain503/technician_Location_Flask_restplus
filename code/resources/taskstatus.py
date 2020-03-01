from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from models.taskstatus import TaskStatusModel


class TaskStatus(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('statusName', type=str, required=True,
                        help='WorkerId is mandatory')

    #
    # @jwt_required()

    def get(self, _id):
        data = TaskStatus.parser.parse_args()
        taskstatus = TaskStatusModel.find_by_id(_id)
        taskstatus.statusName = data['statusName']

        taskstatus.save_to_db()
        return taskstatus.json()
