from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("id", "note", "description")
    search_fields = ("id",)
    empty_value_display = "-пусто-"