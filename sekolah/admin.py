from django.contrib import admin
from .models import Sekolah

class SekolahAdmin(admin.ModelAdmin):
    list_display = ['nama', 'email', 'alamat', ]

admin.site.register(Sekolah, SekolahAdmin)
