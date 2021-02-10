import eventlet
eventlet.monkey_patch()

# Python_____________________
import requests
import json
import re
from datetime import datetime

# Flask__________________________________________
from flask import request
from flask_socketio import SocketIO, send, emit

# DataBase_______________________________________________
from app.database import db
from app.database import r
from flask_login import LoginManager, login_user, current_user, login_required, logout_user


users = {}

socketio = SocketIO()


@socketio.on('add_user')
def connect(user_id):
    # save user session
    r.set(int(user_id), request.sid)
    users.setdefault(int(user_id), request.sid)

    # print DEBUG INFO (remove before prod)
    redis_users_sid = {int(key): r.get(key) for key in r.scan_iter()}
    send('DEBUG INFO' +'\nLocal users sids ' + str(users) + '\nRedis users sids ' + str(redis_users_sid))
