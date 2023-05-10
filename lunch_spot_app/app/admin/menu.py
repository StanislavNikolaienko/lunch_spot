from django.contrib import admin
from ..models import Menu


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')
    search_fields = ('restaurant', 'date')
    list_per_page = 25


admin.site.register(Menu, MenuAdmin)
