from __future__ import absolute_import
from celery import Celery

app = Celery('projplan', include=['projplan.tasks'])

app.config_from_object('projplan.config_crontab')

if __name__ == '__main__':
    app.start()
