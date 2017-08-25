# tasks.py

import time
from celery import Celery

broker = 'redis://localhost:6379/5'
backend = 'redis://localhost:6379/6'

celery = Celery('tasks', broker=broker, backend=backend)


@celery.task
def add(x, y):
    return x + y
