from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from .models import UserProfile

class UpdateUsernameForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username']

class UpdatePasswordForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['password']

class UpdatePreferencesForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['dark_mode']
