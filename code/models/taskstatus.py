

from db import db


class TaskStatusModel(db.Model):

    __tablename__ = 'taskstatus'
    id = db.Column(db.Integer(), primary_key=True)
    statusName = db.Column(db.String(80))

    def __init__(self, statusName):

        self.statusName = statusName
