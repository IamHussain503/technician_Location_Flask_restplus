# task posted before worker can see the task
import datetime
from db import db
from sqlalchemy import func, distinct


class TaskModel(db.Model):

    __tablename__ = 'task'
    id = db.Column(db.Integer(), primary_key=True)
    taskDate = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    taskDetail = db.Column(db.String(512), nullable=True)

    userId = db.Column(db.Integer(), db.ForeignKey('users.id'))
    user = db.relationship('UserModel')
    skillId = db.Column(db.Integer(), db.ForeignKey('skill.id'))
    worker = db.relationship('SkillModel')
    statusId = db.Column(db.integer(), db.ForeignKey('taskstatus.id'))
    taskstatus = db.relationship('TaskStatusModel')

    def __init__(self, userId, skillId, taskDetail, taskDate):

        self.userId = userId
        self.skillId = skillId
        self.taskDate = taskDate
        self.taskDetail = taskDetail

    def json(self):
        return {'id': self.id, 'userId': self.userId,
                "workerId": self.workerId,
                'rating': self.rating, 'comments': self.comments}

    @classmethod
    def find_by_userid_workerid(cls, userId, workerId):
        return cls.query.filter_by(userId=userId, workerId=workerId).first()

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):

        db.session.delete(self)
        db.session.commit()
