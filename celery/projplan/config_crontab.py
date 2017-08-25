from celery.schedules import crontab

CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/5'
BROKER_URL = 'redis://127.0.0.1:6379/6'

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERYBEAT_SCHEDULE ={
    'add-every-3-minutes': {
        'task': 'projplan.tasks.add',
        'schedule': crontab(minute='*/3'),
        'args': (20, 20)
    },
    'add-every-monday-morning': {
        'task': 'projplan.tasks.add',
        'schedule': crontab(hour=12, minute=26),
        'args': (3, 20)
    },
}
