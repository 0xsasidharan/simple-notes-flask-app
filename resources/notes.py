from flask import request
from flask.views import MethodView
from flask_smorest  import Blueprint , abort
from schemas import NotesSchema , NoteUpdateSchema
from uuid import uuid4
from datetime import timezone, datetime
from db import notes

blp = Blueprint("Notes" , __name__ , description="Operation on notes")


@blp.route("/notes")
class NotesListResources(MethodView):
    @blp.response(200,NotesSchema(many=True))
    def get(self):
        return list(notes.values()) , 200

    @blp.arguments(NotesSchema)
    @blp.response(201 , NotesSchema)
    def post(self , request_data):
        
        note_id = uuid4().hex
        today =  datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        new_note = {**request_data , "note_id" :note_id , "created_at" : today}
        notes[note_id] = new_note


        return new_note , 201


@blp.route("/notes/<note_id>")
class NotesResources(MethodView):
    @blp.response(200, NotesSchema)
    def get(self , note_id):
        if note_id not in notes:
            abort(404 , message="Note Id not found")
        return notes[note_id] , 200

    @blp.arguments(NoteUpdateSchema)
    @blp.response(200, NotesSchema)
    def put(self,request_data , note_id):
        

        if note_id not in notes:
            abort(404 , message="Note Id not found")
        
        new_note = request_data
        notes[note_id].update(new_note)

        return notes[note_id] , 200

    @blp.response(200)
    def delete(self , note_id):
        if note_id not in notes:
            abort(404 , message="Note Id not found")
    
        del notes[note_id]
        return {"message" : "Note deleted successfully"} , 200