from flask.ext.classy import FlaskView, route

class DefaultView(FlaskView):
    route_base = '/'

    @route('/')
    def index(self):
        return "Successful installation of flask-skeleton."