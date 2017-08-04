# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.utils import timezone
from django.dispatch import receiver

class UserProfile(models.Model):
    USERGROUP_CHOICES = (
        (0, u'未分配'),
        (1, u'学生'),
        (2, u'老师'),
        (3, u'领导'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # user_is_staff = models.BooleanField(default=False)
    # user_is_active = models.BooleanField(default=True,verbose_name="激活")
    usergroup = models.PositiveSmallIntegerField(choices=USERGROUP_CHOICES, default='0', verbose_name="群组")
    # useremail = models.EmailField (max_length =75)
    # CardID = models.CharField(max_length=200,blank=True)
    # username = models.CharField(
    #     max_length=150,
    #     unique=True,
    #     default=""
    # )
    # first_name = models.CharField(max_length=30, blank=True, default=" ")
    # last_name = models.CharField(max_length=30, blank=True, default=" ")
    # email = models.EmailField(blank=True, default=" ")
    # is_staff = models.BooleanField(default=False,)
    # is_active = models.BooleanField(default=True,)
    # password = models.CharField(max_length=32,default=" ")
    # date_joined = models.DateTimeField(default=timezone.now)
    # class Meta(AbstractUser.Meta):
    #     swappable = 'AUTH_USER_MODEL'
    #     abstract = False

    def __str__(self):
        return self.user.username



@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created,**kwags):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile,sender=User)



