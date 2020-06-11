from flask_mongoengine import MongoEngine
db = MongoEngine()

class Answer(db.Document):
    email = db.StringField(required=True, unique=True)
    student = db.ListField(db.StringField(), required=True)
    value = db.ListField(db.StringField(), required=True)