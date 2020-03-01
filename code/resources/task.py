from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from models.task import TaskModel


class Tasks(Resource):
    parser = reqparse.RequestParser()

    # @jwt_required()

    def put(self, userid, skillid):
        data = Tasks.parser.parse_args()
        # worker = WorkerModel.find_by_id(workerId)
        # worker.mobNum = data['mobNum']

        return
        # worker.json()
