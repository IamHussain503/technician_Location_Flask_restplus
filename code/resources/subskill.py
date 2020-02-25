from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from models.subskill import SubSkillModel


class SubSkill(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('subSkillDetail', required=True,
                        help='subskill Detail is mandatory')

    #
    # @jwt_required()

    def put(self, _id):
        data = SubSkill.parser.parse_args()
        subskill = SubSkillModel.find_by_id(_id)
        subskill.subSkillDetail = data['subSkillDetail']

        subskill.save_to_db()
        return subskill.json()
