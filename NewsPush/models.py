#encoding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django_fsm import FSMField, transition, can_proceed



#Create your models here.

STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
)



class NewsPost(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题")
    author = models.CharField(max_length=50, default=" ",verbose_name="作者")
    cover = models.ImageField(upload_to='Img', verbose_name="封面图")
    body = RichTextUploadingField(blank=True, null=True, verbose_name="内容")
    timestamp = models.DateTimeField(verbose_name="发布时间")
    headline = models.CharField(max_length=50, default=" ", verbose_name="摘要")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d',verbose_name="状态")

    def __unicode__(self):
        return self.title

def make_published(ModelAdmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"

class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'status')




#admin.site.register(NewsPost, NewsPostAdmin)