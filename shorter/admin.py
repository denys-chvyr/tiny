from django.contrib import admin

from shorter.models import Shorter


# Register your models here.

class ShorterAdmin(admin.ModelAdmin):
    search_fields = ['shortened_url']
    list_display = ['shortened_url']
    list_filter = ['shortened_url']

admin.site.register(Shorter, ShorterAdmin)