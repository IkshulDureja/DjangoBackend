from ctypes import alignment
from django.urls import path
from EmployeeApp import views
from EmployeeApp.models import Departments

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('department/', views.departmentApi, name="departments"),
    path('department/<str:id>/', views.departmentApi, name="departments-id"),
    path('employee/', views.employeeApi, name="employees"),
    path('employee/<str:id>/', views.employeeApi, name="employees-id"),
    path('Employee/SaveFile/', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
