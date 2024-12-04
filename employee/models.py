from django.db import models

# Create your Employee models here.

class EmployeeModel(models.Model):
    Emp_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Phone=models.IntegerField()
    Address=models.CharField(max_length=100) 
    DOB=models.DateField()
    Joine_date=models.DateTimeField()
    