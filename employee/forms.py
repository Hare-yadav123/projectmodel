from django import forms
from employee.models import EmployeeModel
from django.forms import widgets,Widget
class ModelForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = ['Name','Email','Phone','Address','DOB','Joine_date']

        widgets = { 
        'Emp_id':forms.NumberInput(attrs={'class':'from-control'}),
        'Name':forms.TextInput(attrs={'class':'from-control'}),
        'Email':forms.EmailInput(attrs={'class':'form-control'}),
        'Phone':forms.NumberInput(attrs={'class':'form-control'}),
        'Addres':forms.TextInput(attrs={'class':'form-control'}),
        'DOB':forms.DateInput(attrs={'class':'form-control'}),
        'Joine_date':forms.DateInput(attrs={'class':'from-control'}),

        }