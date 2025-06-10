from flask import Flask , request
from uuid import uuid4
from datetime import timezone, datetime
from db import notes

app = Flask(__name__)



@app.get("/notes")
def get_notes():
   


    return {"notes" : list(notes.values())} , 200

@app.get("/notes/<note_id>")
def get_one_note(note_id):

    if note_id not in notes:
        return {"error" : "Note Id not found"} , 404
    return {"note" : notes[note_id]} , 200



@app.post("/notes")
def create_notes():
    request_data = request.get_json()

    if ("title" not in request_data):
        return {"message" : "Title is requried"} , 400

    allowed_list = ["title" , "body" ,"tags"]
    for key in request_data: 
        if key not in allowed_list:
            return {"message" : f"This {key} is not allowed"} , 400

    note_id = uuid4().hex
    today =  datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    new_note = {**request_data , "note_id" :note_id , "created_at" : today}
    notes[note_id] = new_note


    return {"notes" : new_note} , 201

@app.put("/notes/<note_id>")
def edit_one_note(note_id):
    request_data = request.get_json()

    if note_id not in notes:
        return {"error" : "Note Id not found"} , 404
    
    allowed_list = ["title" , "body" ,"tags"]
    for key in request_data: 
        if key not in allowed_list:
            return {"message" : f"This {key} is not allowed"} , 400

    new_note = request_data
    notes[note_id].update(new_note)

    return {"note" : new_note} , 200



@app.delete("/notes/<note_id>")
def delet_one_note(note_id):

    if note_id not in notes:
        return {"error" : "Note Id not found"} , 404
    
    del notes[note_id]
    return {"message" : "Note deleted successfully"} , 200