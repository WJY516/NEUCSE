# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-15 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPush', '0003_newspost_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='headline',
            field=models.CharField(default='', max_length=50),
        ),
    ]
