from __future__ import absolute_import, unicode_literals
import os

from pytz import timezone

from celery import Celery
from django.conf import settings



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SmartComp.settings')

app = Celery('SmartComp')
app.conf.enable_utc = False 

app.conf.update(timezone = 'Asia/Kolkata')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')