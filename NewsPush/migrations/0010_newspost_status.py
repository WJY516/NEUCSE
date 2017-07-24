# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-19 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPush', '0009_auto_20170717_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='newspost',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='d', max_length=1),
        ),
    ]
