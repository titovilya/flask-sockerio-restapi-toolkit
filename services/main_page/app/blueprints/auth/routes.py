from datetime import datetime
import json, requests, re
from flask import render_template, url_for, redirect, request, jsonify, flash
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from flask_mail import Mail, Message
from app.blueprints.auth import auth
from app import mail


from app.database import db



serializer = URLSafeTimedSerializer('Thisisabigsecret!')

@auth.route('/test', methods=['GET', 'POST'])
def index():
    
    return render_template('index.html')
