from django.contrib import admin
from .models import Board
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

admin.site.register(Board)