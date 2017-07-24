# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import NewsPost
# Register your models here.

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"

class NewsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'timestamp']
    ordering = ['title']
    actions = [make_published]

admin.site.register(NewsPost,NewsPostAdmin)



