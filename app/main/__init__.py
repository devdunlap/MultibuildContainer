from flask import Blueprint

# Create a Blueprint named 'main'
main = Blueprint('main', __name__)

# Import routes so they are registered with the blueprint
from . import routes