# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Mail, MailReadStatus, Subscribe, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'birthday',
    )
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')
    empty_value_display = '-пусто-'


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user', )
    list_filter = ('user', )
    empty_value_display = '-пусто-'


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = '-пусто-'


@admin.register(MailReadStatus)
class MailReadStatusAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'user',
        'read_status',
    )
    search_fields = (
        'name',
        'user',
    )
    list_filter = (
        'name',
        'user',
    )
    empty_value_display = '-пусто-'
