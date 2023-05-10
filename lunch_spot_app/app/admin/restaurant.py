from django.contrib import admin
from ..models import Restaurant


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number')
    list_display_links = ('name', 'address', 'phone_number')
    list_filter = ('name', 'address')
    search_fields = ('name', 'address')
    list_per_page = 25


admin.site.register(Restaurant, RestaurantAdmin)
