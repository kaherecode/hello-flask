from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def homepage():
        return 'This is the homepage'

    return app
