from django.contrib import admin
from employee.models import EmployeeModel
# Register your models here.
admin.site.register(EmployeeModel)
class UserAdmin(admin.ModelAdmin):
    
    list_display=['Emp_id','Name','Email','Phone','Address','DOB','Joine_date']