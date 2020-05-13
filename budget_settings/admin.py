from django.contrib import admin

from .models import *

admin.site.site_header = "My Money"
admin.site.index_title = "Welcome to My Money Panel Administrator"


@admin.register(Category)
class Category(admin.ModelAdmin):
    ordering = ('Name',)
    search_fields = ('Name',)


@admin.register(Account)
class Account(admin.ModelAdmin):
    list_display = ('Name', 'Comment',)
    ordering = ('Name',)
    search_fields = ('Name',)