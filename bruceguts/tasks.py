from celery import Celery

from .env import CELERY_BROKER

app = Celery(__name__, broker=CELERY_BROKER)


@app.task
def hello():
    return "hello world"
