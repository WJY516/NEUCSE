# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import  UserCreationForm, UserChangeForm

# Register your models here.

# 重新定义增加用户表单，继承UserCreationForm
class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True


# 重新定义编辑用户表单，继承UserChangeForm
class MyUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(MyUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = True


class CustomUserAdmin(UserAdmin):
    def __init__(self, *args, **kwargs):
        super(CustomUserAdmin, self).__init__(*args, **kwargs)
        self.list_display = ('username', 'is_active', 'is_staff', )
        self.search_fields = ('username',)
        self.form = MyUserChangeForm #使用自定义表单
        self.add_form = MyUserCreationForm

admin.site.register(UserProfile,CustomUserAdmin)

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'is_active',)
#     list_editable = ('is_active',)
#
#
# admin.site.register(UserProfile,UserAdmin)