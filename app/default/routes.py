from flask import render_template
from . import default

@default.route('/')
def index():
	return render_template('default/index.html')