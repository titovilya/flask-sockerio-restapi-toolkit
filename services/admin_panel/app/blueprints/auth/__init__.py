from flask import Blueprint
from flask_login import LoginManager
from app.database import db
from app.database.models.admin import Admin


auth = Blueprint('auth', __name__, template_folder='templates/auth', static_folder='static/auth')

login_manager = LoginManager()

@auth.record_once
def on_load(state):
    login_manager.init_app(state.app)

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(user_id)
