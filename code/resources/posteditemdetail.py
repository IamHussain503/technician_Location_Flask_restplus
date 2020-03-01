from flask_restful import Resource, reqparse
import sqlite3
from flask_jwt import jwt_required
from models.posteditemdetail import PostedItemDetailModel


class PostedItemDetail(Resource):
    parser = reqparse.RequestParser()
    # parser.add_argument('quantity', type=int, required=True,
    #                     help='subskill Detail is mandatory')

    def get(self, skillid):
        data = PostedItemDetail.parser.parse_args()
        posted = PostedItemDetailModel.find_by_skillid(skillid)

        return {'posted_item_detail': [x.json() for x in posted]}
