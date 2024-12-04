from django.shortcuts import render
from .models import StuModel
# Create your views here.

def stu(request):
    # context={'name':'Haree'}
    if request.method=='POST':
        form=StuModel(request.POST)
        if form.is_valid():
            form.save()
        else:
            form=StuModel()
    else:
        form=StuModel()
    fm=StuModel.objects.all()
    return render(request,'student/index.html',{'form':form})