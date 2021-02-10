import os
import sys
import traceback
from functools import reduce
from app.config import Config
import requests, json, re
import eventlet
requests = eventlet.import_patched("requests") #NOT DELETE WITHOUT ANY Q
from datetime import datetime, timedelta
from flask import render_template, url_for, redirect, request, flash, jsonify
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from app.blueprints.main_page import main_page
from werkzeug.security import check_password_hash, generate_password_hash

# Database Models___________________________________________________
from app.database import db


# Main Variables_________________________________________


@main_page.route('/', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html')
