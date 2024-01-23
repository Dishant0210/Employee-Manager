# Employee Manager

Employee Manager is a minimal Django-based web application for managing employees, departments, and employee salaries. It consists of three modules:

1. **Employee Management**: Add, update, and delete employee records. Define employee attributes such as name, email, address, and designation. Employees belong to a specific department and have a reporting manager.

2. **Department Management**: Administer departments by adding, updating, and deleting department records. View the employee hierarchy within each department, showcasing managers, team leads, and associates.

3. **Employee Salary Management**: Record and manage employee salaries over time. Admins can add, update, and delete salary entries for employees, specifying salary changes within date ranges.

## Features

- **Employee Management:**
  - Add, update, and delete employees.
  - Assign designations, reporting managers, and departments.

- **Department Management:**
  - Add, update, and delete departments.
  - View the hierarchical structure of employees within each department.

- **Employee Salary Management:**
  - Add, update, and delete salary entries.
  - Generate reports on department-wise salary costs for a given date range.

**Navigate to the project directory:**
-cd employee-management-system

**Create and activate a virtual environment:**
python -m venv myenv
myenv\Scripts\activate`

**Apply database migrations:**
python manage.py makemigrations
python manage.py migrate

**Run the development server:**
 python manage.py runserver

**Usage**
Access the Django admin interface to manage employees, departments, and salaries:
http://127.0.0.1:8000/admin/

**Credintals for Django admin page**
 username:dishant
 password:123456

Use the provided views and templates to interact with the Employee Management, Department Management, and Employee Salary Management modules.

