from celery import Celery

from .env import CELERY_BROKER
from . import builds

app = Celery(__name__, broker=CELERY_BROKER)
# TODO: setup results backend.


@app.task
def hello():
    builds.build()
    return "hello world"


hello()
