from django.contrib import admin
from models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'spling_code', 'image')
    ordering = ('parent', 'id')

admin.site.register(Category, CategoryAdmin)
