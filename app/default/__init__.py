from flask import Blueprint
default = Blueprint('cast', __name__)
from . import routes