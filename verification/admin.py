from django.contrib import admin
from .models import Statement, Tag


@admin.register(Statement)
class StatementAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_at", "updated_at")
    list_filter = ("status", "tags")
    search_fields = ("title", "text", "author")
    autocomplete_fields = ("tags",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ("name",)
