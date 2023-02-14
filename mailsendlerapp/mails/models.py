# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    '''Model user.'''
    birthday = models.DateTimeField('День рождения',
                                    blank=False,
                                    default=timezone.now)
    email = models.EmailField('Почта',blank=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='subscruber',
                             verbose_name='Подписчик')

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'


class Mail(models.Model):
    name = models.CharField('Название файла',
                            blank=False,
                            unique=True,
                            max_length=50)

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'


class MailReadStatus(models.Model):
    name = models.ForeignKey(Mail,
                             on_delete=models.CASCADE,
                             related_name='file',
                             verbose_name='Название файла')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='reader',
                             verbose_name='Подписчик')
    read_status = models.BooleanField(blank=False, default=False)

    class Meta:
        verbose_name = 'Статус прочтения письма'
        verbose_name_plural = 'Статусы прочтенных писем'
