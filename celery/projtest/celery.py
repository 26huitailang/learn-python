from celery import Celery

app = Celery('projtest', include=['projtest.tasks'])

app.config_from_object('projtest.config')

if __name__ == '__main__':
    app.start()
