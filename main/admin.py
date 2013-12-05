from django.contrib import admin
from models import *

class PromotionInline(admin.TabularInline):
    model = Promotion

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'position', 'show_in_menu', 'show_in_video', 'show_in_shop', 'spling_code')
    list_editable = ('position', 'show_in_menu', 'show_in_video', 'show_in_shop',)
    ordering = ('parent__id', 'position')
    prepopulated_fields = {"slug": ("name",)}
    inlines = [PromotionInline,]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Promotion)
