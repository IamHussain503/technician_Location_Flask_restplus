from flask_restful import Resource, reqparse
from flask import jsonify, make_response
import sqlite3
from flask_jwt import jwt_required
from models.subskill import SubSkillModel


class SubSkill(Resource):
    parser = reqparse.RequestParser()
    # parser.add_argument('subSkillDetail', required=True,
    #                     help='subskill Detail is mandatory')

    #
    # @jwt_required()

    def get(self, skillid):
        subskill = SubSkillModel.find_by_skillid(skillid)

        return {'subSkillDetail': [x.json() for x in subskill]}
