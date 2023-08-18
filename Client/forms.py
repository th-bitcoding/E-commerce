from django import forms
from Client.models import Client,Category
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields=['first_name','email','address','gender','DOB','phone_number','image']
        widgets = {
            'DOB': forms.DateInput(attrs = {'style': 'front-size: 13px; cursor: pointer', 'type':'date','onkeydown': 'return false'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields=['id','category']
        