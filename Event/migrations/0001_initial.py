# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-23 09:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.FileField(upload_to='')),
                ('location', models.CharField(max_length=250)),
                ('date', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('payment', models.CharField(choices=[('free', 'Free'), ('not Free', 'Not free')], default='Free', max_length=10)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
