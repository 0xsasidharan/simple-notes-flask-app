from db import db

class NoteModel(db.Model):
    __tablename__ = "notes"
    note_id = db.Column(db.Integer ,primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    created_at = db.Column(db.String, nullable=False)
    body = db.Column(db.String)
    tags = db.Column(db.PickleType)