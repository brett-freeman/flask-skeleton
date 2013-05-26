from flask.ext.classy import FlaskView, route
from flask import render_template

class DefaultView(FlaskView):
    route_base = '/'

    @route('/')
    def index(self):
        return render_template('index.html')