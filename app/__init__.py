from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def homepage():
        return render_template('homepage.html')

    @app.route('/about/')
    def about():
        return render_template('about.html')

    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name='diallo'):
        return render_template('hello.html', name=name)

    return app
