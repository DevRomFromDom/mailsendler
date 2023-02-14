import os
import sys

from django.core.wsgi import get_wsgi_application

sys.dont_write_bytecode = True

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mailsendlerapp.settings")

application = get_wsgi_application()
