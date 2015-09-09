# -*- coding: utf-8 -*- 

from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['content', 'date']
    search_fields = ['content']
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Feedback, FeedbackAdmin)
