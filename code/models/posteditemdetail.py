# list of detailed jobs selected by the customer and calculate estimated price based on number of jobs
import datetime
from db import db
from sqlalchemy import func, distinct
import sqlite3
from flask_marshmallow import Marshmallow
from models.posteditemstatus import PostedItemStatusModel


class PostedItemDetailModel(db.Model):

    __tablename__ = 'posted_item_detail'

    id = db.Column(db.Integer(), primary_key=True)
    postDate = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    quantity = db.Column(db.Integer(), nullable=False)
    rate = db.Column(db.Integer(), nullable=False)
    total = db.Column(db.Integer(), nullable=False)

    subSkillId = db.Column(db.Integer(), db.ForeignKey('subskills.id'))
    subskill = db.relationship('SubSkillModel')
    skillId = db.Column(db.Integer(), db.ForeignKey('skills.id'))
    skill = db.relationship('SkillModel')
    statusId = db.Column(db.Integer(), db.ForeignKey(
        'taskstatus.id'), default=0)
    taskstatus = db.relationship('TaskStatusModel')
    postedItemStatusId = db.Column(
        db.Integer(), db.ForeignKey('posted_Item_status.id'), default=2)
    posteditemstatus = db.relationship('PostedItemStatusModel')
    taskId = db.Column(db.Integer(), db.ForeignKey('tasks.id'))
    task = db.relationship('TaskModel')

    def __init__(self, quantity, rate, total):

        self.quantity = quantity
        self.rate = rate
        self.total = total
        self.subSkillId = subSkillId
        self.skillId = skillId
        self.postedItemStatusId = postedItemStatusId
        self.postDate = postDate
        self.taskId = taskId

    def json(self):
        return {'id': self.id, 'quantity': self.quantity, "rate": self.rate,
                'total': self.total, 'subSkillId': self.subSkillId,
                'skillId': self.skillId, 'postedItemStatusId': self.postedItemStatusId,
                'postDate': self.postDate, 'taskId': self.taskId}

    @classmethod
    def find_by_skillid(cls, skillId):
        return cls.query.filter_by(skillId=skillId)

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):

        db.session.delete(self)
        db.session.commit()
