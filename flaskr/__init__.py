import os
import requests
from flask import Flask, render_template
import db
from views import earnings_bp

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    DEBUG=True,
)
db.init_app(app)
app.register_blueprint(earnings_bp)


@app.route('/')
def index():
    return render_template('Home.html')


@app.route('/hello/')
def hello():
    return 'Hello, World!'


def scraper_app(test_config=None):
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


if __name__ == "__main__":
    app.run()

