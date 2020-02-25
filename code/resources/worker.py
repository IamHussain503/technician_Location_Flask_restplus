from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from models.worker import WorkerModel


class Worker(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('idCard', type=str, required=True,
                        help='this field can not be left blank')
    parser.add_argument('skillId', type=int, required=True,
                        help='Skill ID is mandatory')
    # @jwt_required()
    def get(self, mobNum):

        worker = WorkerModel.find_by_name(mobNum)
        if worker:
            return worker.json()
        return {'message': 'worker not found'}, 404

    # def get(self, workerId):

    #     worker = WorkerModel.find_by_id(workerId)
    #     if worker:
    #         return worker.json()
    #     return {'message': 'worker not found'}, 404

    def post(self, mobNum):

        if WorkerModel.find_by_name(mobNum):
            return {'message': 'An worker with mobNum {} alerady exists'
                    .format(mobNum)}, 400
        data = Worker.parser.parse_args()
        worker = WorkerModel(mobNum, **data)
        try:
            worker.save_to_db()
        except:
            return {'message': 'An error has occured, try again later'}, 500

        return worker.json(), 201

    def delete(self, mobNum):
        worker = WorkerModel.find_by_name(mobNum)
        if worker:
            worker.delete_from_db()
            return {'message': 'worker has been deleted'}
        else:
            return {'message': 'worker does not exist'}

    def put(self, mobNum):
        data = Worker.parser.parse_args()
        # updated_worker = WorkerModel(mobNum, data**)
        worker = WorkerModel.find_by_name(mobNum)
        if worker is None:
            worker = WorkerModel(mobNum, **data)
        else:
            worker = WorkerModel(mobNum, **data)

        worker.save_to_db()
        return worker.json()


class WorkerList(Resource):
    # @jwt_required()
    def get(self):
        return {'workers': [x.json() for x in WorkerModel.query.all()]}


class WorkerById(Resource):
    # @jwt_required()
    def get(self, workerId):
        worker = WorkerModel.find_by_id(workerId)
        if worker:
            return worker.json()
        return {'message': 'worker not found'}, 404


class WorkerBySkillId(Resource):
    # @jwt_required()
    def get(self, _skillid):
        worker = WorkerModel.find_by_skillid(_skillid)
        # print(worker)
        if worker:
            return {'workers': [x.json() for x in worker]}
        return {'message': 'worker not found'}, 404
