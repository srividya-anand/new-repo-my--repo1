from django.contrib import admin
from myapp.models import Employee
class EmployeeAdmin(admin.ModelAdmin):
    l=['eid','ename','eage','eexp','esal']
admin.site.register(Employee,EmployeeAdmin)    

# Register your models here.
