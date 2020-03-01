from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from models.assigned import AssignModel


class Assign(Resource):
    parser = reqparse.RequestParser()

    # parser.add_argument('idCard', type=str, required=True,
    #                     help='this field can not be left blank')
    # parser.add_argument('skillId', type=int, required=True,
    #                     help='Skill ID is mandatory')
    # @jwt_required()
    def get(self, taskid):

        assign = AssignModel.find_by_taskid(taskid)
        if assign:
            return assign.json()
        return {'message': 'assign not found'}, 404

    # def get(self, workerId):

    #     assign = AssignModel.find_by_id(workerId)
    #     if assign:
    #         return assign.json()
    #     return {'message': 'assign not found'}, 404

    def post(self, taskId, workerId):

        if AssignModel.find_by_taskid_workerid(taskId, workerId):
            return {'message': 'An assign with ID {} and task number {} alerady exists'
                    .format(workerId, taskId)}, 400
        data = Assign.parser.parse_args()
        assign = AssignModel(taskId, workerId, **data)
        try:
            assign.save_to_db()
        except:
            return {'message': 'An error has occured, try again later'}, 500

        return assign.json(), 201

    def delete(self, taskId, workerId):
        assign = AssignModel.find_by_taskid_workerid(taskId, workerId)
        if assign:
            assign.delete_from_db()
            return {'message': 'assign has been deleted'}
        else:
            return {'message': 'assign does not exist'}

    def put(self, taskId, workerId):
        data = Assign.parser.parse_args()
        # updated_worker = AssignModel(mobNum, data**)
        assign = AssignModel.find_by_taskid_workerid(taskId, workerId)
        if assign is None:
            assign = AssignModel(taskId, workerId, **data)
        else:
            assign = AssignModel(taskId, workerId, **data)

        assign.save_to_db()
        return assign.json()


class AssignList(Resource):
    # @jwt_required()
    def get(self):
        return {'qoutes': [x.json() for x in AssignModel.query.all()]}


class AssignById(Resource):
    # @jwt_required()
    def get(self, workerId):
        assign = AssignModel.find_by_id(workerId)
        if assign:
            return assign.json()
        return {'message': 'assign not found'}, 404


class AssignBySkillId(Resource):
    # @jwt_required()
    def get(self, _skillid):
        assign = AssignModel.find_by_skillid(_skillid)
        # print(assign)
        if assign:
            return {'assign': [x.json() for x in assign]}
        return {'message': 'assign not found'}, 404
