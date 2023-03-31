from django.contrib import admin
from .models import Notes
from . import models


# Register your models here.

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(models.Notes, NotesAdmin)
