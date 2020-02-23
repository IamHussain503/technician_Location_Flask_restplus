# from db import db


# class RatingStarModel(db.Model):

#     __tablename__ = 'ratingstars'

#     star1 = db.Column(db.Integer(64), default=0)
#     star2 = db.Column(db.Integer(64), default=0)
#     star3 = db.Column(db.Integer(64), default=0)
#     star4 = db.Column(db.Integer(64), default=0)
#     star5 = db.Column(db.Integer(64), default=0)

#     workerId = db.Column(db.Integer, db.ForeignKey('workers.id'))
#     worker = db.relationship('WorkerModel')

#     def __init__(self, workerId, star1, star2, star3, star4, star5):

#         self.workerId = workerId
#         self.star1 = star1
#         self.star2 = star2
#         self.star3 = star3
#         self.star4 = star4
#         self.star5 = star5
