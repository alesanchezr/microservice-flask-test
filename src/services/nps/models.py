from flask_mongoengine import MongoEngine
db = MongoEngine()

class Answer(db.Document):
    email = db.StringField(required=True, unique=True)
    student = db.StringField(required=True)
    value = db.StringField(required=True)