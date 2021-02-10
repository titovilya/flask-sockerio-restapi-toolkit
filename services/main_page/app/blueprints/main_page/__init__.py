from flask import Blueprint
from flask_login import LoginManager


main_page = Blueprint('main_page', __name__, template_folder='templates/main_page', static_folder='static/main_page')
