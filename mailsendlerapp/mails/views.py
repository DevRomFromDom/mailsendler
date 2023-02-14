from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView

from .models import Mail, MailReadStatus, User
from .tasks import send_email_task


class DefaultView(TemplateView):
    template_name = 'mail.html'


def email_opened(request, filename, email):
    user = get_object_or_404(User, email=email)
    mail = get_object_or_404(Mail, name=filename)
    email_status, _ = MailReadStatus.objects.get_or_create(user=user,
                                                           name=mail)
    if email_status.read_status is False:
        email_status.read_status = True
        email_status.save()
        return HttpResponse(status=201)
    return HttpResponse(status=200)


def send_emails(request):
    send_email_task.apply_async(countdown=10)
    return HttpResponse(status=200, content='<h1>Email was sended</h1>')
