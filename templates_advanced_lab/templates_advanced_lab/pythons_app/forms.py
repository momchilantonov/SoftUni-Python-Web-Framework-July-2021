from .models import Python
from django import forms


class PythonCreateForm(forms.ModelForm):
    class Meta:
        model = Python
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
        
