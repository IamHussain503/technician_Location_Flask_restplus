import sqlite3
import datetime
from db import db


class AssignModel(db.Model):

    __tablename__ = 'assign'

    id = db.Column(db.Integer(), primary_key=True)
    assignDate = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    price = db.Column(db.Numeric(), nullable=False)

    userId = db.Column(db.Integer(), db.ForeignKey('users.id'))
    user = db.relationship('UserModel')
    skillId = db.Column(db.Integer(), db.ForeignKey('skills.id'))
    skill = db.relationship('SkillModel')
    workerId = db.Column(db.Integer(), db.ForeignKey('workers.id'))
    worker = db.relationship('WorkerModel')
    taskId = db.Column(db.Integer(), db.ForeignKey('tasks.id'))
    task = db.relationship('TaskModel')
    state = db.Column(db.Integer(), db.ForeignKey(
        'taskstatus.id'), default=0)
    taskstatus = db.relationship('TaskStatusModel')

    def __init__(self, state,  assignDate, taskId):

        self.state = state
        self.price = price
        self.assignDate = assignDate
        # self.taskId = taskId

    def json(self):
        return {'id': self.id, 'state': self.state,
                'assignDate': self.assignDate, 'userId': self.userId, 'skillId': self.skillId,
                'workerId': self.workerId, 'taskId': self.taskId, 'price': self.price}

    @classmethod
    def find_by_taskid(cls, taskid):
        print(cls.query.filter_by(taskId=taskid))
        return cls.query.filter_by(taskId=taskid)

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):

        db.session.delete(self)
        db.session.commit()
