from flask import request
from flask.views import MethodView
from flask_smorest  import Blueprint , abort
from schemas import NotesSchema , NoteUpdateSchema
from datetime import timezone, datetime
from db import db
from models.notes import NoteModel

blp = Blueprint("Notes" , __name__ , description="Operation on notes")


@blp.route("/notes")
class NotesListResources(MethodView):
    @blp.response(200,NotesSchema(many=True))
    def get(self):
        tag = request.args.get("tag")
        notes_list = NoteModel.query.all()
        
        if tag:
            tag = tag.lower()
            filtered_list = []
            for note in notes_list:
                if note.tags and isinstance(note.tags, list):
                    if any(t.lower() == tag for t in note.tags):
                        filtered_list.append(note)

            if not filtered_list:
                abort(404, message=f"No notes found with tag '{tag}'")
            return filtered_list
        
        return notes_list

    @blp.arguments(NotesSchema)
    @blp.response(201 , NotesSchema)
    def post(self , request_data):
        
        today =  datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        
        
        new_note = NoteModel(
            created_at=today,
            title=request_data.get("title"),
            body=request_data.get("body"),
            tags=request_data.get("tags", [])
        )
        db.session.add(new_note)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(500 , message="Database error while creating note")
        return new_note


@blp.route("/notes/<int:note_id>")
class NotesResources(MethodView):
    @blp.response(200, NotesSchema)
    def get(self , note_id):
        note = NoteModel.query.get(note_id)
        if note is None:
            abort(404 , message="Note Id not found")
        return note

    @blp.arguments(NoteUpdateSchema)
    @blp.response(200, NotesSchema)
    def put(self,request_data , note_id):
        note = NoteModel.query.get(note_id)

        if note is None:
            abort(404 , message="Note Id not found")
        
        if "title" in request_data:
            note.title = request_data["title"]
        if "body" in request_data:
            note.body = request_data["body"]
        if "tags" in request_data:
            note.tags = request_data["tags"]        
        
        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(500 ,message="Database error while creating task" )

        return note

    @blp.response(200)
    def delete(self , note_id):
        note = NoteModel.query.get(note_id)
        if note is None:
            abort(404 , message="Note Id not found")

        db.session.delete(note)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(500, message="Database error while deleting task")
        return {"message" : "Note has been deleted successfully"}
