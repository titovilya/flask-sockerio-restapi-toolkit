import sys
import traceback
from app import application
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy(application)
migrate = Migrate(application, db)

from .models import (
    #import each model separately
)

