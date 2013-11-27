from django.contrib import admin
from models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'spling_code', 'background', 'article')
    ordering = ('parent', 'id')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)
