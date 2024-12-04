from django.shortcuts import render,HttpResponseRedirect
from employee.models import EmployeeModel
from. forms import ModelForm
from .models import EmployeeModel
# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm=ModelForm(request.POST)   
        if fm.is_valid():
            fm.save()
            # nm=fm.cleaned_data['Name']
            # em=fm.cleaned_data['Email']
            # pn=fm.cleaned_data['Phone']
            # ad=fm.cleaned_data['Address']
            # da=fm.cleaned_data['DOB']
            # jd=fm.cleaned_data['Joine_date']
            # reg=EmployeeModel(name=nm, email=em,phone=pn, address=ad, date=da, join=jd)
            # reg.save() 
        fm=ModelForm()   
    else:
        fm=ModelForm()
    std=EmployeeModel.objects.all()
    return render(request, 'employee/addandshow.html',{'form':fm ,'stu':std})

# delete function 

def delete_data(request, id):
    if request.method == 'POST':
        ob=EmployeeModel.objects.get(pk=id)
        ob.delete()
        return HttpResponseRedirect('/')


# update form
def update_data(request,id):
    if request.method=='PUT':
        id=EmployeeModel.objects.get(pk=id)
        fm=ModelForm(request.PUT,instance=id)
        if fm.is_valid():
            fm.save()
    else:
       id=EmployeeModel.objects.get(pk=id)
       fm=ModelForm(instance=id)
    return render(request, 'employee/update.html' ,{'form':fm})