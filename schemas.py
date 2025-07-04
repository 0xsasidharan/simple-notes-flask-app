from marshmallow import Schema , fields

class NotesSchema(Schema):
    note_id = fields.Integer(dump_only=True)
    created_at = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    body = fields.Str()
    tags = fields.List(fields.Str())

class NoteUpdateSchema(Schema):
    title = fields.Str()
    body = fields.Str()
    tags = fields.List(fields.Str())