import timeit
from datetime import datetime
import json, requests
from flask import render_template, url_for, redirect, request
from app.blueprints.admin_panel import admin_panel
from app.database import db



@admin_panel.route('/', methods=['GET'])
def index():
    return render_template('index.html')

