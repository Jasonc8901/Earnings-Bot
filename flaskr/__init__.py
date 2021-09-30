import os
import requests
from flask import Flask

from flaskr import db


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)


@app.route('/')
def index():
    return 'Home route.'


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

    db.init_app(app)

    return app


if __name__ == "__main__":
    app.run()

