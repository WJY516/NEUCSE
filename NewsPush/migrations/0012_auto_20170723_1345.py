# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-23 05:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsPush', '0011_auto_20170723_1321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspost',
            name='author',
        ),
        migrations.AlterField(
            model_name='newspost',
            name='headline',
            field=models.CharField(default=' ', max_length=50, verbose_name='\u6458\u8981'),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published'), ('w', 'Withdrawn')], default='d', max_length=1, verbose_name='\u72b6\u6001'),
        ),
    ]
