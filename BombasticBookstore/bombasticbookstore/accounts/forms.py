
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Inherit Django's default UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50) # Required
    last_name = forms.CharField(max_length=50) # Required
    email = forms.EmailField() # Required
    # All fields you re-define here will become required fields in the form

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']