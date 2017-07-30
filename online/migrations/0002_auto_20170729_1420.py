# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='userrank',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='usergroup',
            field=models.CharField(choices=[('0', '\u672a\u5206\u914d'), ('1', '\u5b66\u751f'), ('2', '\u8001\u5e08'), ('3', '\u9886\u5bfc')], default='0', max_length=1, verbose_name='\u7fa4\u7ec4'),
        ),
    ]
