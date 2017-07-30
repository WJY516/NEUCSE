# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import Group, AbstractUser
from django.db.models.signals import post_save
from django.utils import timezone

class UserProfile(AbstractUser):
    # GROUP_CHOICES = (
    #     ('0', u'未分配'),
    #     ('1', u'学生'),
    #     ('2', u'老师'),
    #     ('3', u'领导'),
    # )
    # user = models.CharField(max_length=32, null=False, blank=False, )
    # user_is_staff = models.BooleanField(default=False)
    # user_is_active = models.BooleanField(default=True,verbose_name="激活")
    # usergroup = models.CharField(max_length=1, choices=GROUP_CHOICES, default='0',verbose_name="群组")
    # useremail = models.EmailField (max_length =75)
    CardID = models.CharField(max_length=200,blank=True)
    username = models.CharField(
        max_length=150,
        unique=True,
        default=""
    )
    first_name = models.CharField(max_length=30, blank=True, default=" ")
    last_name = models.CharField(max_length=30, blank=True, default=" ")
    email = models.EmailField(blank=True, default=" ")
    is_staff = models.BooleanField(default=False,)
    is_active = models.BooleanField(default=True,)
    password = models.CharField(max_length=32,default=" ")
    date_joined = models.DateTimeField(default=timezone.now)
    # class Meta(AbstractUser.Meta):
    #     swappable = 'AUTH_USER_MODEL'
    #     abstract = False





# def create_user_profile(sender,instance,created,**kwags):
#     if created:
#         UserProfile.objects.create(user=instance)
#
# post_save.connect(create_user_profile,sender=User)



