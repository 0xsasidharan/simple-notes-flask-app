from marshmallow import Schema , fields

class NotesSchema(Schema):
    note_id = fields.Str(dump_only=True)
    created_at = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    body = fields.Str()

class NoteUpdateSchema(Schema):
    title = fields.Str()
    body = fields.Str()
