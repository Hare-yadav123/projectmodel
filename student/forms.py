from models import StuModel
from django import forms

class StuForm(forms.ModelForm):
    class Meta:
        model=StuModel
        fields=['name','mobile']