from django.contrib import admin
from models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'position', 'show_in_menu', 'show_in_video', 'show_in_shop', 'spling_code')
    list_editable = ('position', 'show_in_menu', 'show_in_video', 'show_in_shop',)
    ordering = ('parent__id', 'position')
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Category, CategoryAdmin)
