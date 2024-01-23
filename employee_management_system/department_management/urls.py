from django.urls import path
from .views import department_list

urlpatterns = [
    path('departments/', department_list, name='department_list'),
    # ... other paths for department views
]
