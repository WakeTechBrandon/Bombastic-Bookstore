from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from .forms import UserSettingsForm

# Login requirement is commented out for testing purposes
# @login_required
def user_settings(request):
	if request.method == 'POST':
		if request.user.is_authenticated:
			form = UserSettingsForm(request.POST, instance=request.user)
		else:
			form = UserSettingsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('settings')
	else:
		if request.user.is_authenticated:
			form = UserSettingsForm(instance=request.user)
		else:
			form = UserSettingsForm()
	return render(request, 'user_settings/user_settings.html', {'form': form})

# Create your views here.
