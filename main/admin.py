from django.contrib import admin
from models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'position', 'spling_code', 'background', 'article')
    list_editable = ('position', )
    list_filter = ('parent',)
    ordering = ('parent__id', 'position')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)
