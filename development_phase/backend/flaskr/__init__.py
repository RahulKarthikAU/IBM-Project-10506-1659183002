from flask import Flask
from flask_cors import CORS
from flask_restful import Api, reqparse

parser = reqparse.RequestParser()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    CORS(app)

    from .controllers.auth import Register
    api.add_resource(Register, '/api/auth/register')

    @app.route('/hello')
    def hello():
        return 'Hello, World'
    
    return app