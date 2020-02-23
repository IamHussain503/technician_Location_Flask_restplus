
import datetime
from db import db


class WorkerModel(db.Model):

    __tablename__ = 'workers'

    id = db.Column(db.Integer(), primary_key=True)
    mobNum = db.Column(db.String(80), nullable=False, unique=True)
    # price = db.Column(db.Float(precision=2))
    fName = db.Column(db.String(80), nullable=True)
    mName = db.Column(db.String(80), nullable=True)
    lName = db.Column(db.String(80), nullable=True)
    mobNum = db.Column(db.String(80))
    email = db.Column(db.String(80), nullable=True)
    joinDate = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    idCard = db.Column(db.String(80))

    skillId = db.Column(db.Integer(), db.ForeignKey('skills.id'))
    skill = db.relationship('SkillModel')

    def __init__(self, mobNum, idCard, skillId):

        self.mobNum = mobNum
        self.idCard = idCard
        self.skillId = skillId

    def json(self):
        return {'mobNum': self.mobNum, 'id': self.id,
                "idCard": self.idCard, 'skill_id': self.skillId}

    @classmethod
    def find_by_name(cls, mobNum):
        return cls.query.filter_by(mobNum=mobNum).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_skillid(cls, _skillid):
        return cls.query.filter_by(skillId=_skillid)

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):

        db.session.delete(self)
        db.session.commit()
