# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_web', models.CharField(max_length=30)),
                ('tagline_web', models.CharField(blank=True, max_length=50, null=True)),
                ('description_web', models.TextField(blank=True, null=True)),
                ('logo_web', models.FileField(upload_to=b'')),
            ],
        ),
    ]
