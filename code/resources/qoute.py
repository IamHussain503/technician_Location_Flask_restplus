from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from models.qoute import QouteModel


class Qoute(Resource):
    parser = reqparse.RequestParser()

    # parser.add_argument('idCard', type=str, required=True,
    #                     help='this field can not be left blank')
    # parser.add_argument('skillId', type=int, required=True,
    #                     help='Skill ID is mandatory')
    # @jwt_required()
    def get(self, taskid):

        qoute = QouteModel.find_by_taskid(taskid)
        if qoute:
            return qoute.json()
        return {'message': 'qoute not found'}, 404

    # def get(self, workerId):

    #     qoute = QouteModel.find_by_id(workerId)
    #     if qoute:
    #         return qoute.json()
    #     return {'message': 'qoute not found'}, 404

    def post(self, taskId, workerId):

        if QouteModel.find_by_taskid_workerid(taskId, workerId):
            return {'message': 'An qoute with ID {} and task number {} alerady exists'
                    .format(workerId, taskId)}, 400
        data = Qoute.parser.parse_args()
        qoute = QouteModel(taskId, workerId, **data)
        try:
            qoute.save_to_db()
        except:
            return {'message': 'An error has occured, try again later'}, 500

        return qoute.json(), 201

    def delete(self, taskId, workerId):
        qoute = QouteModel.find_by_taskid_workerid(taskId, workerId)
        if qoute:
            qoute.delete_from_db()
            return {'message': 'qoute has been deleted'}
        else:
            return {'message': 'qoute does not exist'}

    def put(self, taskId, workerId):
        data = Qoute.parser.parse_args()
        # updated_worker = QouteModel(mobNum, data**)
        qoute = QouteModel.find_by_taskid_workerid(taskId, workerId)
        if qoute is None:
            qoute = QouteModel(taskId, workerId, **data)
        else:
            qoute = QouteModel(taskId, workerId, **data)

        qoute.save_to_db()
        return qoute.json()


class QouteList(Resource):
    # @jwt_required()
    def get(self):
        return {'qoutes': [x.json() for x in QouteModel.query.all()]}


class QouteById(Resource):
    # @jwt_required()
    def get(self, workerId):
        qoute = QouteModel.find_by_id(workerId)
        if qoute:
            return qoute.json()
        return {'message': 'qoute not found'}, 404


class QouteBySkillId(Resource):
    # @jwt_required()
    def get(self, _skillid):
        qoute = QouteModel.find_by_skillid(_skillid)
        # print(qoute)
        if qoute:
            return {'qoutes': [x.json() for x in qoute]}
        return {'message': 'qoute not found'}, 404
