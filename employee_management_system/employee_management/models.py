from django.db import models
class Employee(models.Model):
    DESIGNATION_CHOICES = [
        ('Associate', 'Associate'),
        ('TL', 'Team Lead'),
        ('Manager', 'Manager'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.TextField()
    designation = models.CharField(max_length=20, choices=DESIGNATION_CHOICES)
    reporting_manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey('department_management.Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
