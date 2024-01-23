from django.contrib import admin
from .models import Salary

class SalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'salary_amount', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    search_fields = ('employee__name',)

admin.site.register(Salary, SalaryAdmin)
