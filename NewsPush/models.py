#encoding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.utils import timezone
from django_fsm import FSMField, transition, can_proceed



#Create your models here.

class PublishedManager(models.Manager):
   def get_queryset(self):
       return super(PublishedManager,self).get_queryset().filter(status='p')

class NewsPost(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    title = models.CharField(max_length=100, verbose_name="标题")
    author = models.ForeignKey(User, related_name='newspost')
    cover = models.ImageField(upload_to='Img', verbose_name="封面图")
    body = RichTextUploadingField(blank=True, null=True, verbose_name="内容")
    timestamp = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True,null=True)
    updated = models.DateTimeField(auto_now=True)
    headline = models.CharField(max_length=50, default=" ", verbose_name="摘要")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d',verbose_name="状态")

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('-timestamp',)

    objects = models.Manager()  # The default manager
    published = PublishedManager()  # Our custom manager

def make_published(ModelAdmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"

class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'status')




#admin.site.register(NewsPost, NewsPostAdmin)