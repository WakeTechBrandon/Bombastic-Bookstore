from django import forms
from django.contrib.auth.models import User

class UserSettingsForm(forms.ModelForm):
	email = forms.EmailField(required=True)
	password = forms.CharField(widget=forms.PasswordInput, required=False)
	theme = forms.ChoiceField(choices=[('light', 'Light Mode'), ('dark', 'Dark Mode')], required=True)

	class Meta:
		model = User
		fields = ['email', 'password', 'theme']

	def save(self, commit=True):
		user = super().save(commit=False)
		if self.cleaned_data['password']:
			user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user