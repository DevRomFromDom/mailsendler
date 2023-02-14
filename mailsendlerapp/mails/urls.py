from django.conf.urls import url

from .views import DefaultView, email_opened, send_emails

app = 'mails'

urlpatterns = [
    url('sendemailswithcelery', view=send_emails, name='send_emails'),
    url(regex=(
        r'^OPENED/(?P<filename>[\w.@+-]+)/(?P<email>\w+|[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$'
    ),
        view=email_opened,
        name='email_opened'),
    url('mails', DefaultView.as_view(), name='mail')
]
