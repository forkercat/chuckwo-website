from django.contrib import admin

from .models import Pet, Statistics

class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'pic', 'hot')

class StatisticsAdmin(admin.ModelAdmin):
    readonly_feilds = ['name', 'visits', 'clicks']
    list_display = ['name', 'visits', 'clicks']
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Pet, PetAdmin)
admin.site.register(Statistics, StatisticsAdmin)
