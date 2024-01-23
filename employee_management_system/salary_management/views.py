from django.shortcuts import render
from django.db.models import Sum
from .models import Salary
from employee_management.models import Employee 
from department_management.models import Department

def salary_list(request):
    salaries = Salary.objects.all()
    return render(request, 'salary_management/salary_list.html', {'salaries': salaries})

def salary_report(request):
    salaries = Salary.objects.all()
    return render(request, 'salary_management/report.html', {'salaries': salaries})

def department_salary_cost_report(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # Perform data validation and calculations
        # Ensure start_date and end_date are in the correct format and handle errors

        # Calculate department-wise salary cost
        department_costs = Salary.objects.filter(start_date__gte=start_date, end_date__lte=end_date) \
                        .values('employee__department__name') \
                        .annotate(total_cost=Sum('salary_amount'))

        return render(request, 'salary_management/department_salary_cost_report.html', {'department_costs': department_costs})

    return render(request, 'salary_management/department_salary_cost_report.html')
