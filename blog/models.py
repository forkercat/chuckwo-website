from django.db import models
from django.contrib import admin
from tinymce.models import HTMLField

class Header(models.Model):
    title = models.CharField(max_length=150)
    intro = models.CharField('Introduction', max_length=150)

    def __unicode__(self):
        return self.title

class BlogsPost(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    # body = models.TextField()
    body = HTMLField()
    timestamp = models.DateTimeField('Date')
    like = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title