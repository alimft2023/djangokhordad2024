from django import forms 
from django.forms import ModelForm
from .models import Post

class PostCreateForm(forms.Form):
    title=forms.CharField()
    body=forms.CharField()
    created=forms.DateTimeField()
    
class PostUpdateForm(ModelForm):
    class Meta:
        model=Post 
        fields="__all__"