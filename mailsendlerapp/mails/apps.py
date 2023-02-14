# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

from django.apps import AppConfig

sys.dont_write_bytecode = True


class MailsConfig(AppConfig):
    name = 'mails'
