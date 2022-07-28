from flask import Blueprint
routes = Blueprint('routes', __name__)

from .reading import *
from .test import *