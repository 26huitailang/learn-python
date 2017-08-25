from projtest.celery import app
import time

@app.task
def add(x, y):
    time.sleep(20)
    return x + y
