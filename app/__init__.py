from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def homepage():
        return 'This is the homepage'

    @app.route('/about/')
    def about():
        return 'This is the about page'

    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name='diallo'):
        return 'Hello {}!'.format(name.capitalize())

    return app
