#!/usr/bin/python3


from flask import Flask
from flask_restx import Api
from app.api.v1.users import api as users_ns
from app.api.v1.amenities import api as amenities_ns
from app.api.v1.places import api as place_ns
from app.api.v1.reviews import api as reviews_ns
from app.api.v1.auth import api as login_ns
from app.api.v1.admins import api as admins_ns
from app.extensions import bcrypt, jwt, db
from flask_cors import CORS

def create_app(config_class="config.DevelopmentConfig"):
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config_class)
    api = Api(app, version='1.0', title='HBnB API', description='HBnB Application API', doc='/api/v1/')
    bcrypt.init_app(app)
    jwt.init_app(app)
    db.init_app(app)


    api.add_namespace(users_ns, path='/api/v1/users')
    api.add_namespace(amenities_ns, path='/api/v1/amenities')
    api.add_namespace(place_ns, path='/api/v1/places')
    api.add_namespace(reviews_ns, path='/api/v1/reviews')
    api.add_namespace(login_ns, path='/api/v1/auth')
    api.add_namespace(admins_ns, path='/api/v1/admins')

    """ CORS. resources tell flask to only apply CORS to /api/.
    Allows any frontend running on localhost on any port. support_credentials as True allows auth headers"""
    CORS(app, resources={r"/api/v1/.*": {"origins": [
        r"http://localhost:\d+",
        r"http://127.0.0.1:\d+"]}}, supports_credentials=True)

    return app
