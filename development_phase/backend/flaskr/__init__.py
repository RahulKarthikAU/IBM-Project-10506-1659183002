from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    from .utils.db import run_sql
    run_sql('select * from user where id = ? and email = ?', (1, 'hello@124',))

    @app.route('/hello')
    def hello():
        return 'Hello, World'
    
    return app