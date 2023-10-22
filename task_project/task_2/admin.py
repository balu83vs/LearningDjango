from django.contrib import admin
from .models import NoteUsers, Notes

# Register your models here.

admin.site.register(NoteUsers)
admin.site.register(Notes)
