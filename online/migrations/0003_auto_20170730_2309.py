# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0002_auto_20170730_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='usergroup',
            field=models.PositiveSmallIntegerField(choices=[(0, '\u672a\u5206\u914d'), (1, '\u5b66\u751f'), (2, '\u8001\u5e08'), (3, '\u9886\u5bfc')], default='0', verbose_name='\u7fa4\u7ec4'),
        ),
    ]
