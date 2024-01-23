from django.db import models
from employee_management.models import Employee

class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.salary_amount}"
