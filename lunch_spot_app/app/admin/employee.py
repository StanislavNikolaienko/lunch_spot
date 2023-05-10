from django.contrib import admin
from ..models import Employee


class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    list_display_links = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('department', 'position')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number', 'department')
    list_per_page = 25


admin.site.register(Employee, EmployeesAdmin)
