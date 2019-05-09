from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from models.db import db, ma
from models.note import Note

class Notebook(db.Model):
    __tablename__ = 'notebooks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    creation_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
    notes = db.relationship("Note", cascade="all,delete", backref = "notebooks")
    
    def __init__(self, title, creation_date):
        self.title = title
        self.creation_date = creation_date


class NotebookSchema(ma.Schema):
    id = fields.Integer()
    title = fields.String(required=True)
    creation_date = fields.DateTime()