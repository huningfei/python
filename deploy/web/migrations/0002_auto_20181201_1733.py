# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-01 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='git',
            field=models.CharField(max_length=128, verbose_name='仓库地址'),
        ),
    ]
