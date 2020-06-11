import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property


import os, sys
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__))+'/../../')
from flask_restful_swagger import swagger
from flask_restful import Resource
from flask import request
from .models import db, Answer
from app import API

api = API(db)

class Endpoints(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        body = request.get_json()
        answer = Answer(**body).save()
        return answer.to_json()

api.add_resource(Endpoints, "/"+os.path.basename(os.path.dirname(os.path.realpath(__file__))))

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    api.run(host='0.0.0.0', port=PORT, debug=True)