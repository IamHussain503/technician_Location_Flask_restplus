# the status of each item pending , done , expire etc...
import datetime
from db import db
from sqlalchemy import func, distinct
import sqlite3


class QouteStateModel(db.Model):

    __tablename__ = 'qoutestate'

    id = db.Column(db.Integer(), primary_key=True)
    state = db.Column(db.String(80))

    def __init__(self, state):

        self.status = status

    def save_to_db(self):

        db.session.add(self)
        db.session.commit()
