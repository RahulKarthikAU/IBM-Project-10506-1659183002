from flask import Flask
from flask_cors import CORS
from flask_restful import Api, reqparse

parser = reqparse.RequestParser()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    api = Api(app)
    CORS(app)

    from .controllers.auth import Register, Login, VerifyEmail
    api.add_resource(Register, '/api/auth/register')
    api.add_resource(Login, '/api/auth/login')
    api.add_resource(VerifyEmail, '/api/auth/verify')

    @app.route('/hello')
    def hello():
        return 'Hello, World'

    @app.after_request
    def after_request(res):
        res.headers['Access-Control-Allow-Origin'] = 'http://localhost:5500'
        res.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        res.headers['Access-Control-Expose-Headers'] = 'true'
        res.headers['Access-Control-Allow-Credentials'] = 'true'
        return res
        
    return app