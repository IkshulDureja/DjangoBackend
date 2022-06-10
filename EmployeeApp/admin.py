from django.contrib import admin

# Register your models here.
from .models import Departments, Employees

admin.site.register(Departments)
admin.site.register(Employees)
