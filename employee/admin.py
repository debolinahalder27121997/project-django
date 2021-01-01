from django.contrib import admin
from employee.models import Employee,leavedetail,emptime
admin.site.register(leavedetail)
admin.site.register(Employee)
admin.site.register(emptime)
# Register your models here.
