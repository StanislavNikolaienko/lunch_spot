from django.contrib import admin
from ..models import Poll


class PollAdmin(admin.ModelAdmin):
    list_display = ('employee', 'restaurant', 'date')
    list_filter = ('employee','date')
    search_fields = ('employee', 'date')
    list_per_page = 25


admin.site.register(Poll, PollAdmin)
