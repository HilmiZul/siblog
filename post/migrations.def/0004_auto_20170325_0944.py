# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20170325_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='feature_image',
            field=models.FileField(upload_to='/upload/'),
        ),
    ]
