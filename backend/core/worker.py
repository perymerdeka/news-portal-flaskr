from core import celery_ext
from core.factory import create_app
from core.utils.celery import init_celery

app = create_app()
init_celery(app=app, celery=celery_ext)