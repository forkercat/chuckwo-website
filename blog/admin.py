
from django.contrib import admin
from .models import Header, BlogsPost



class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'timestamp', 'like']
    search_fields = ['title', 'author', 'body']
    readonly_fields = ['like']


class HeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'intro']
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False



admin.site.register(Header, HeaderAdmin)
admin.site.register(BlogsPost, BlogsPostAdmin)