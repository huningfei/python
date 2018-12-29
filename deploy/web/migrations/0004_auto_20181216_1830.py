# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-12-16 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20181201_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='private',
            field=models.BooleanField(default=True, verbose_name='是否私有'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(max_length=64, verbose_name='密码'),
        ),
    ]
