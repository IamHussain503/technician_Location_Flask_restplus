# task posted before worker can see the task
import datetime
from db import db
from sqlalchemy import func, distinct
import sqlite3


class TaskModel(db.Model):

    __tablename__ = 'tasks'
    id = db.Column(db.Integer(), primary_key=True)
    taskDate = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    # taskDetail = db.Column(db.String(512), nullable=True)
    # assignDate = db.Column(db.DateTime, default=None)
    userId = db.Column(db.Integer(), db.ForeignKey('users.id'))
    user = db.relationship('UserModel')
    skillId = db.Column(db.Integer(), db.ForeignKey('skills.id'))
    skill = db.relationship('SkillModel')
    statusId = db.Column(db.Integer(), db.ForeignKey(
        'taskstatus.id'), default=0)
    taskstatus = db.relationship('TaskStatusModel')

    # workerId = db.Column(db.Integer(), db.ForeignKey(
    #     'workers.id'), default=0)
    # worker = db.relationship('WorkerModel')

    def __init__(self, userId, skillId, taskDetail, taskDate):

        self.userId = userId
        self.skillId = skillId
        self.taskDate = taskDate
        self.taskDetail = taskDetail

    def json(self):
        return {'id': self.id, 'userId': self.userId,
                'rating': self.rating, 'comments': self.comments}

    @classmethod
    def find_by_userid_workerid(cls, userId):
        return cls.query.filter_by(userId=userId).first()

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):

        db.session.delete(self)
        db.session.commit()
