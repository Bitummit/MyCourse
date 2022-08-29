import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyCourse.settings')

course_app = Celery('course', backend='rpc://')
course_app.config_from_object('django.conf:settings', namespace='CELERY')
course_app.autodiscover_tasks()
