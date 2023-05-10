from django.contrib import admin
from ..models import Dish


class DishAdmin(admin.ModelAdmin):
    list_display = ("price", "description")
    search_fields = ("menu", "name")
    list_per_page = 25


admin.site.register(Dish, DishAdmin)
