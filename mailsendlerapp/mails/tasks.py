from django.core.management import call_command
from celery import shared_task

from .functions import send_messege


@shared_task
def send_email_task():
    send_messege(filename='mail.html')
