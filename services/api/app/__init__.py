from flask import Flask
from app.config import Config
from flask_restless import APIManager


application = Flask(__name__)
application.config.from_object(Config)

import app.database as database


api_manager = APIManager(application, flask_sqlalchemy_db=database.db)

from app import api
