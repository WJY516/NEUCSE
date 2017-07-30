# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save

class UserProfile(models.Model):
    GROUP_CHOICES = (
        ('0', u'未分配'),
        ('1', u'学生'),
        ('2', u'老师'),
        ('3', u'领导'),
    )
    user = models.OneToOneField(User)
    user_is_staff = models.BooleanField(default=False)
    user_is_active = models.BooleanField(default=True,verbose_name="激活")
    usergroup = models.CharField(max_length=1, choices=GROUP_CHOICES, default='0',verbose_name="群组")
    #useremail = models.EmailField (max_length =75)



    #def __unicode__(self):
        #return self.username





def create_user_profile(sender,instance,created,**kwags):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile,sender=User)



