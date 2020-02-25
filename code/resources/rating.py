from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.rating import RatingModel


class Rating(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('rating', type=int, required=True,
                        help='userId field can not be left blank')
    parser.add_argument('comments', type=str, required=False,
                        help='rating field can not be left blank',
                        action='append')

    # @jwt_required()
    def get(self, userId, workerId):

        rating = RatingModel.find_by_name(userId, workerId)
        if rating:
            return rating.json()
        return {'message': 'rating not found'}, 404

    def post(self, userId, workerId):
        data = Rating.parser.parse_args()
        print(data)
        if RatingModel.find_by_userid_workerid(userId, workerId):
            return {'message': 'An rating with userId, workerId {} alerady exists'
                    .format(userId, workerId)}, 400

        #data = request.get_json()
        rating = RatingModel(userId, workerId, **data)
        try:
            rating.save_to_db()
        except:
            return {'message': 'An error has occured, try again later'}, 500

        return rating.json(), 201


class RatingUpdate(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('rating', type=int, required=True,
                        help='userId field can not be left blank')
    parser.add_argument('comments', type=str, required=False,
                        help='rating field can not be left blank',
                        action='append')
    parser.add_argument('workerId', type=int, required=True,
                        help='userId field can not be left blank')
    parser.add_argument('userId', type=int, required=True,
                        help='rating field can not be left blank',
                        action='append')

    def put(self, ratingId):

        data = RatingUpdate.parser.parse_args()
        rating = RatingModel.find_by_ratingid(ratingId)
        if rating:
            rating.comments = data['comments']
            rating.rating = data['rating']

            rating.save_to_db()
            return rating.json()
        else:
            return {'message': 'there is no rating found for this user'}, 400


class AvgRating(Resource):

    def get(self, workerId):
        rating = RatingModel.avg_by_workerid(workerId)
        if rating:
            return rating

        return {'messsage': 'There are no reviews yet'}


class RatingCount(Resource):

    def get(self, workerId):
        ratingcount = RatingModel.rating_count(workerId)
        if ratingcount:
            return ratingcount
        else:
            return {'message': 'There is no rating yet'}


class DistinctRatingCount(Resource):

    def get(self, workerId):
        ratingcount = RatingModel.distinct_rating_count(workerId)
        if ratingcount:
            return ratingcount
        else:
            return {'message': 'There is no rating yet'}
