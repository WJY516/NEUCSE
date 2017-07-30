# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('user',  'usergroup', 'user_is_active',)
    list_editable = ('usergroup', 'user_is_active' )


admin.site.register(UserProfile,UserAdmin)