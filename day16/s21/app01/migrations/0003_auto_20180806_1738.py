# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-06 09:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Publisher',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]