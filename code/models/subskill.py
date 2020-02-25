# sub skill means that how many kinds of sub catagory are avaialble for each Skill catagory
# initially to be addded by the user from database, later it can be added by a administrator using web interface
import datetime
from db import db
from sqlalchemy import func, distinct


class SubSkillModel(db.Model):

    __tablename__ = 'subskills'
    id = db.Column(db.Integer(), primary_key=True)
    subSkillDetail = db.Column(db.String(90), nullable=True)

    skillId = db.Column(db.Integer(), db.ForeignKey('skills.id'))
    skill = db.relationship('SkillModel')

    def __init__(self, SubSkillModel, skillId):

        self.subSkillDetail = subSkillDetail
        self.skillId = skillId

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()
