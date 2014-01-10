from django.contrib import admin
from .models import Woning

class WoningAdmin(admin.ModelAdmin):
    list_display = ("straat", "huisnummer", "plaats",)

admin.site.register(Woning, WoningAdmin)
