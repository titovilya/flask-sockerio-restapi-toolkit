import json, ast, requests, re
from flask import render_template, url_for, redirect, request, jsonify, flash
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from app.blueprints.auth import auth
from app.models import Admin


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_panel.index'))

    
    admin_login = request.form.get('admin_login')
    password = request.form.get('password')
    
    if admin_login and password:
        requests_filter = json.dumps({
            'filters': [
                {
                    'name': 'login',
                    'op': 'eq',
                    'val': admin_login
                }
            ]
        })

        admins = json.loads(requests.get(f'http://api/api/v1/admin_panel_users?q={requests_filter}').content.decode('utf-8'))['objects']
        
        if admins and check_password_hash(admins[0]['password'], password):
            new_user = Admin(admins[0]['id'])
            login_user(new_user)
            return redirect(url_for('admin_panel.index'))

        flash('Неверный логин или пароль')
        return render_template('login.html')
    
    return render_template('login.html')


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/create', methods=['GET', 'POST'])
def create():
    new_user = {
            'name': 'Admin',
            'password': generate_password_hash('root'),
            'login': 'root',
        }

    json.loads(requests.post('http://api/api/v1/admin_panel_users', data=json.dumps(new_user), headers={'content-type': 'application/json'}).content.decode('utf-8'))
    return redirect(url_for('auth.login'))
