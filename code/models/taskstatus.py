# how many status of tasks 1) not assigned 2) assigned 3) accomlished 4) expired etc...

from db import db


class TaskStatusModel(db.Model):

    __tablename__ = 'taskstatus'
    id = db.Column(db.Integer(), primary_key=True)
    statusName = db.Column(db.String(80))

    def __init__(self, statusName):

        self.statusName = statusName

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()
