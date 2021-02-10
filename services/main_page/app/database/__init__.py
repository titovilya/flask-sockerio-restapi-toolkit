import redis
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
r = redis.StrictRedis(host='redis', decode_responses=True, port=6379, db=1)
