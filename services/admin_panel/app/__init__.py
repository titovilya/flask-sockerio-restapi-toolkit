from flask import Flask
from app.config import Config
from flask_wtf.csrf import CSRFProtect


csrf = CSRFProtect()

def create_app(config):
    app = Flask(__name__)
    
    app.config.from_object(config)

    csrf.init_app(app)
    
    with app.app_context():
        from app.blueprints.admin_panel.routes import admin_panel
        app.register_blueprint(admin_panel)
    
    return app

app = create_app(Config)
