# -*- coding: utf-8 -*- 

from django.db import models

class Feedback(models.Model):
    content = models.TextField(u'反馈内容', max_length=200, default='')
    date = models.DateTimeField(u'日期')

    def __unicode__(self):
        return 'Feedback'
