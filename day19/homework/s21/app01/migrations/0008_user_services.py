# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-22 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_auto_20180815_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='services',
            field=models.ManyToManyField(related_name='user', to='app01.Service'),
        ),
    ]
