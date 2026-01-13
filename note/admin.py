from django.contrib import admin
from note.models import Note

class NoteAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_per_page = 4
    list_filter = ['created_at']
    list_display = ['id', 'name', 'created_at']

# Register your models here.
admin.site.register(Note, NoteAdmin)