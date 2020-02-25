from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    mobNum = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, mobNum, password):
        self.mobNum = mobNum
        self.password = password

    def json(self):
        return {'mobNum': self.mobNum, 'id': self.id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, mobNum):
        return cls.query.filter_by(mobNum=mobNum).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_mobile(cls, _mobNum):
        return cls.query.filter_by(mobNum=_mobNum)
