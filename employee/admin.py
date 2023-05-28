from django.contrib import admin

from employee.models import Employee

# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone',
                    'email', 'salary', 'gender', 'jobtype']
    search_fields = ['name', 'phone', 'email']
    list_filter = ['gender', 'jobtype']
    list_per_page = 10


admin.site.register(Employee, EmployeeAdmin)
