#the status of each item pending , done , expire etc...
import datetime
from db import db
from sqlalchemy import func, distinct


class PostedItemStatusModel(db.Model):

    __tablename__ = 'posted_Item_status'
    id = db.Column(db.Integer(), primary_key=True)
    status = db.Column(db.String(90), nullable=False)

    def __init__(self, status):

        self.status = status

