from flask import Flask, send_from_directory, g, session, flash
from flask.ext.sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.before_request
def before_request():
    pass

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
        'favicon.ico', mimetype='image/vnd.microsoft.icon')

from app.views.default import DefaultView
DefaultView.register(app)