# favorites/admin.py
from django.contrib import admin
from .models import Favorite

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'item_type', 'item_id', 'added_at')  # поля из модели
    search_fields = ('user__email', 'item_type')
    list_filter = ('item_type', 'added_at')  # только существующие поля
