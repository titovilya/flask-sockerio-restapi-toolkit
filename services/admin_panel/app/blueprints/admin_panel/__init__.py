from flask import Blueprint


admin_panel = Blueprint('admin_panel', __name__, template_folder='templates/admin_panel', static_folder='static/admin_panel')
