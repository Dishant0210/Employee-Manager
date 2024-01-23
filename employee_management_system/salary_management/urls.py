from django.urls import path
from .views import salary_list, salary_report, department_salary_cost_report

urlpatterns = [
    path('salaries/', salary_list, name='salary_list'),
    path('report/', salary_report, name='salary_report'),
    path('department_salary_cost_report/', department_salary_cost_report, name='department_salary_cost_report'),
    # ... other paths for salary views
]
