# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 04:08
from __future__ import unicode_literals

from django.db import migrations
#import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='biodata',
            #field=tinymce.models.HTMLField(),
        ),
    ]
