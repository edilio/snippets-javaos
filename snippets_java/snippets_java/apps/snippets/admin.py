from django.contrib import admin
from .models import *


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_filter = ('created_by', 'created_on')
    list_display = ('title', 'language', 'style', 'created_on', 'created_by')
    search_fields = ('title', 'code')

    readonly_fields = ('created_by', )

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()