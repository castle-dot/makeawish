from django.contrib import admin
from .models import AdBar

@admin.register(AdBar)
class AdBarAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'display_order', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title',)