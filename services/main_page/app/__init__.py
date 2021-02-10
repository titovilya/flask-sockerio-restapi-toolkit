import eventlet
eventlet.monkey_patch()
import os
import re
from datetime import datetime
from flask import Flask
from app.config import Config
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail


from app.database import db
from app.websockets.events import socketio


csrf = CSRFProtect()
mail = Mail()


def create_app(config):
    app = Flask(__name__)
    
    app.config.from_object(config)

    csrf.init_app(app)

    db.init_app(app)

    mail.init_app(app)
    
    socketio.init_app(app, async_mode='eventlet', cors_allowed_origins=["https://servername.com", "https://www.servername.com"], message_queue=os.environ.get('CELERY_BROKER_URL'))

    with app.app_context():
        from app.blueprints.auth.routes import auth
        from app.blueprints.main_page.routes import main_page


        app.register_blueprint(auth)
        app.register_blueprint(main_page)
    
    return app

app = create_app(Config)
