# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-23 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='booking_on',
        ),
        migrations.RemoveField(
            model_name='table',
            name='duration',
        ),
    ]