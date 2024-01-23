from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'designation', 'reporting_manager', 'department')
    list_filter = ('designation', 'department')
    search_fields = ('name', 'email')

admin.site.register(Employee, EmployeeAdmin)
