"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
# from flask_cors import CORS
# from utils import APIException, generate_sitemap
from flask import Flask
from flask_restful import Api
from flask_restful_swagger import swagger




class API:

    def __init__(self,db, testing=False):
        app = Flask(__name__)
        app.url_map.strict_slashes = False
        api = swagger.docs(Api(app), apiVersion='0.1')
        # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
        # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        app.config['MONGODB_SETTINGS'] = { 
            'host': 'mongodb://localhost/movie-bag' 
        }
        db.init_app(app)
        # MIGRATE = Migrate(app, db)
        # db.init_app(app)
        # CORS(app)

        self.app = app
        self.api = api

    def get_app(self):
        return self.app

    def add_resource(self, *args):
        return self.api.add_resource(*args)

    def run(self, **kwargs):
        self.app.run(**kwargs)










#from models import Person



# # Handle/serialize errors like a JSON object
# @app.errorhandler(APIException)
# def handle_invalid_usage(error):
#     return jsonify(error.to_dict()), error.status_code

# # generate sitemap with all your endpoints
# @app.route('/')
# def sitemap():
#     return generate_sitemap(app)

# @app.route('/hello', methods=['POST', 'GET'])
# def handle_hello():

#     response_body = {
#         "hello": "world"
#     }

#     return jsonify(response_body), 200

# # this only runs if `$ python src/main.py` is executed