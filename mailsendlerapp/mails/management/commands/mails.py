# -*- coding: utf-8 -*-
import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.apps import apps
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from dotenv import load_dotenv


load_dotenv()

class Command(BaseCommand):
    EMAIL_ADDRES = os.getenv('EMAIL_ADDRES')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    help = "Отправка email html-макета всем подписчикам."
    
    def handle(self, *args, **kwargs):
        # Получение всех моделей приложения mails
        app_models = [
            model for model in apps.get_app_config('mails').get_models()
        ]
        user_model = [x for x in app_models if x.__name__ == 'User'][0]
        Mail_model = [x for x in app_models if x.__name__ == 'Mail'][0]
        subscribe_model = [x for x in app_models
                           if x.__name__ == 'Subscribe'][0]
        # Получение подписчиков
        subs = user_model.objects.filter(pk__in = subscribe_model.objects.all())
        
        # Создаем запись о шаблоне письма который мы собираемся отправить в рассылку
        _ , _ = Mail_model.objects.get_or_create(name=filename)
        
        port_url = 'http://127.0.0.1:8000'
        msg = MIMEMultipart()
        msg['Subject'] = 'Hi. It`s your new email!'
        msg['From'] = self.EMAIL_ADDRES
        filename = 'mail.html'
        s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        s.login(self.EMAIL_ADDRES, self.EMAIL_PASSWORD)
        for sub in subs:
            body_msg = render_to_string(filename,
                                        context={'filename':filename,
                                            'email_reader':sub.email,
                                            'port_url': port_url,
                                            'first_name': sub.first_name,
                                            'last_name': sub.last_name,
                                            'birthday': sub.birthday
                                        }).encode('utf-8')
            msg['To'] = sub.email
            msg.attach(MIMEText(body_msg, 'html')) 
            s.sendmail(self.EMAIL_ADDRES, sub.email, msg.as_string())
        s.quit()