
import datetime
from db import db
from sqlalchemy import func, distinct


class RatingModel(db.Model):

    __tablename__ = 'rating'
    id = db.Column(db.Integer(), primary_key=True)
    rating = db.Column(db.Integer(), nullable=False)
    rateDate = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    comments = db.Column(db.String(512), nullable=True)

    userId = db.Column(db.Integer(), db.ForeignKey('users.id'))
    user = db.relationship('UserModel')
    workerId = db.Column(db.Integer(), db.ForeignKey('workers.id'))
    worker = db.relationship('WorkerModel')

    def __init__(self, userId, workerId, rating, comments):

        self.userId = userId
        self.workerId = workerId
        self.rating = rating
        self.comments = comments

    def json(self):
        return {'id': self.id, 'userId': self.userId,
                "workerId": self.workerId,
                'rating': self.rating, 'comments': self.comments}

    @classmethod
    def find_by_userid_workerid(cls, userId, workerId):
        return cls.query.filter_by(userId=userId, workerId=workerId).first()

    @classmethod
    def find_by_ratingid(cls, _ratingId):
        return cls.query.filter_by(id=_ratingId).first()

    @classmethod
    def avg_by_workerid(cls, _workerId):
        return {'avg': [str(c[0]) for c in db.session.query
                        (func.avg(RatingModel.rating))
                        .filter_by(workerId=_workerId)]}

    # @classmethod
    # def rating_count(cls, _workerId):
    #     return {'rating_count': [str(c[0]) for c in db.session.query
    #                              (func.count(RatingModel.rating))
    #                              .filter_by(workerId=_workerId)]}

    @classmethod
    def rating_count(cls, _workerId):
        return {'count': cls.query.with_entities(func.count(RatingModel.rating))
                .filter_by(workerId=_workerId).scalar()}

    @classmethod
    def distinct_rating_count(cls, _workerId):
        rating = dict(cls.query.with_entities
                      (RatingModel.rating, func.count(
                          RatingModel.rating))
                      .group_by(RatingModel.rating)
                      .filter_by(workerId=_workerId))
        return rating

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):

        db.session.delete(self)
        db.session.commit()
