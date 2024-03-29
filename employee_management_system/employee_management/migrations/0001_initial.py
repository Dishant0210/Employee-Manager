# Generated by Django 5.0.1 on 2024-01-17 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField()),
                ('designation', models.CharField(choices=[('Associate', 'Associate'), ('TL', 'Team Lead'), ('Manager', 'Manager')], max_length=20)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department_management.department')),
                ('reporting_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee_management.employee')),
            ],
        ),
    ]
