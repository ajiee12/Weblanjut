from django.contrib import admin
from .models import Datadiri

class DatadiriAdmin(admin.ModelAdmin):
    list_display = ('user', 'alamat','telp')
admin.site.register(Datadiri, DatadiriAdmin)
