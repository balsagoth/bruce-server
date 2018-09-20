from celery import Celery

from .env import CELERY_BROKER

app = Celery(__name__, broker=CELERY_BROKER)
# TODO: setup results backend.


@app.task
def hello():
    return "hello world"
