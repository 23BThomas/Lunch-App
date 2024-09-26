"""lunch_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from lunch_app.views import redeem_lunch
from lunch_app.views import employee_list, add_employee, edit_employee, delete_employee

urlpatterns = [
    path('admin/', admin.site.urls),
    path('redeem/', redeem_lunch, name='redeem'),
    # Employee management URLs
    path('employees/', employee_list, name='employee_list'),
    path('employees/add/', add_employee, name='add_employee'),
    path('employees/edit/<int:employee_id>/', edit_employee, name='edit_employee'),
    path('employees/delete/<int:employee_id>/', delete_employee, name='delete_employee'),
]