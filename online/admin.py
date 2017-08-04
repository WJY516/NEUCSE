# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import  UserCreationForm, UserChangeForm

from .models import UserProfile

# Register your models here.

# 重新定义增加用户表单，继承UserCreationForm
# class MyUserCreationForm(UserCreationForm):
#     def __init__(self, *args, **kwargs):
#         super(MyUserCreationForm, self).__init__(*args, **kwargs)
#         self.fields['name'].required = True
#
#
# # 重新定义编辑用户表单，继承UserChangeForm
# class MyUserChangeForm(UserChangeForm):
#     def __init__(self, *args, **kwargs):
#         super(MyUserChangeForm, self).__init__(*args, **kwargs)
#         self.fields['name'].required = True
#
#
# class CustomUserAdmin(UserAdmin):
#     def __init__(self, *args, **kwargs):
#         super(CustomUserAdmin, self).__init__(*args, **kwargs)
#         self.list_display = ('username', 'is_active', 'is_staff', )
#         self.search_fields = ('username',)
#         self.form = MyUserChangeForm #使用自定义表单
#         self.add_form = MyUserCreationForm
#
# admin.site.register(UserProfile,CustomUserAdmin)

# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'is_active',)
#     list_editable = ('is_active',)
#
#
# admin.site.register(UserProfile,UserAdmin)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    list_display = ('username', 'is_active', 'is_staff', 'get_group',)
    list_select_related = ('userprofile', )
    list_editable = ('is_active', 'is_staff',)

    def get_group(self,instance):
        return instance.userprofile.usergroup
    get_group.short_description = 'rank'

    def get_groups(self,obj):
        return self.groups
    # get_group.short_description = 'group'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)