# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-27 06:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('gender', models.SmallIntegerField(choices=[(0, '女'), (1, '男'), (2, '保密')], default=2)),
                ('age', models.IntegerField()),
            ],
            options={
                'verbose_name': '作者',
                'verbose_name_plural': '作者',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True)),
                ('publisher_date', models.DateField(auto_now_add=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('authors', models.ManyToManyField(to='app01.Author')),
            ],
            options={
                'verbose_name': '书名',
                'verbose_name_plural': '书名',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='出版社名字')),
                ('address', models.TextField(verbose_name='出版社地址')),
            ],
            options={
                'verbose_name': '出版社',
                'verbose_name_plural': '出版社',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publisher'),
        ),
    ]