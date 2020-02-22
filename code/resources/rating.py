from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.rating import RatingModel


class Rating(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('userId', type=int, required=True,
                        help='userId field can not be left blank')
    parser.add_argument('workerId', type=int, required=True,
                        help='rating field can not be left blank')
    parser.add_argument('rating', type=int, required=True,
                        help='rating field can not be left blank')

    # @jwt_required()
    def get(self, userId, workerId):

        rating = RatingModel.find_by_name(userId, workerId)
        if rating:
            return rating.json()
        return {'message': 'rating not found'}, 404

    def post(self, userId, workerId):
        data = Rating.parser.parse_args()
        if RatingModel.find_by_name(userId, workerId):
            return {'message': 'An rating with userId, workerId {} alerady exists'
                    .format(userId, workerId)}, 400

        #data = request.get_json()
        rating = RatingModel(userId, workerId, **data)
        try:
            rating.save_to_db()
        except:
            return {'message': 'An error has occured, try again later'}, 500

        return rating.json(), 201

    def put(self, userId, workerId):
        data = Rating.parser.parse_args()
        # updated_worker = RatingModel(userId, workerId, data**)
        rating = RatingModel.find_by_name(userId, workerId)
        if rating is None:
            rating = RatingModel(userId, workerId, **data)
        else:
            rating = RatingModel(userId, workerId, **data)

        rating.save_to_db()
        return rating.json()
