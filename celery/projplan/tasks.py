from projplan.celery import app
import time

@app.task
def add(x, y):
    print('seerf')
    return x + y
