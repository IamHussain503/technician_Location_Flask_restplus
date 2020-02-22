from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from models.worker import WorkerModel


class WorkerMobUpdate(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('mobNum', type=str, required=True,
                        help='WorkerId is mandatory')
    parser.add_argument('idCard', type=str, required=True,
                        help='WorkerId is mandatory')
    parser.add_argument('skillId', type=str, required=True,
                        help='WorkerId is mandatory')
    #
    # @jwt_required()

    def put(self, workerId):
        data = WorkerMobUpdate.parser.parse_args()
        worker = WorkerModel.find_by_id(workerId)
        worker.mobNum = data['mobNum']

        worker.save_to_db()
        return worker.json()
