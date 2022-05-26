from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from flask_appbuilder import Model


class data_nego(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(150), unique=True, nullable=False)
    topic = db.Column(db.String(200),  unique=True, nullable=False)
    chapter = db.Column(db.String(200),  unique=True, nullable=False)
    commentaire = db.Column(db.String(),  unique=True, nullable=False)
    def __init__(self, subject, topic, chapter, commentaire):
        self.subject = subject
        self.topic = topic
        self.chapter = chapter
        self.commentaire = commentaire