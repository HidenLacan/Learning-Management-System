from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUser



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields =  UserCreationForm.Meta.fields 

class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password")