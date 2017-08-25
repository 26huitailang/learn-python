from __future__ import absolute_import
from datetime import timedelta

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/5'
BROKER_URL = 'redis://127.0.0.1:6379/6'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERYBEAT_SCHEDULE = {
    'add-every-10-seconds': {
        'task': 'projplan.tasks.add',
        'schedule': timedelta(seconds=10),
        'args': (10, 20)
    },
}
