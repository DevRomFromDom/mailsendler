from __future__ import absolute_import

import os

from django.apps import apps

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mailsendlerapp.settings")

app = Celery('mailsendlerapp')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
