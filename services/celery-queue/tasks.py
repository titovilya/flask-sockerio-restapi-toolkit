import os
import time
from datetime import datetime
from celery import Celery
from celery.task.schedules import crontab
from celery.decorators import periodic_task

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

# CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
# CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery_app = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


celery_app.conf.beat_schedule = {
    "see-you-in-ten-seconds-task": {
        "task": "tasks.name",
        "schedule": 40.0
    }
}

@celery_app.task(name='tasks.name')
def check():
    #function to do
    pass
