# -*- coding: utf-8 -*-
import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.template.loader import render_to_string
from dotenv import load_dotenv

from models import User, Subscribe, Mail

load_dotenv()

def send_messege(filename):
    """Отправка сообщений всем подписчикам."""
    EMAIL_ADDRES = os.getenv('EMAIL_ADDRES')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    
    # Создаем запись о шаблоне письма который мы собираемся отправить в рассылку
    _ , _ = Mail.objects.get_or_create(name=filename)
    
    # Получение подписчиков
    subs = User.objects.filter(pk__in = Subscribe.objects.all())
    
    port_url = 'http://127.0.0.1:8000'
    msg = MIMEMultipart()
    msg['Subject'] = 'Hi. It`s your new email!'
    msg['From'] = EMAIL_ADDRES
    
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(EMAIL_ADDRES, EMAIL_PASSWORD)
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
        s.sendmail(EMAIL_ADDRES, sub.email, msg.as_string())
    s.quit()