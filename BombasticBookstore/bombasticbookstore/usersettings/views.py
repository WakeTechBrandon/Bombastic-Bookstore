from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UpdateUsernameForm, UpdatePasswordForm, UpdatePreferencesForm
from .models import UserProfile

@login_required
def user_settings(request):
    if not hasattr(request.user, 'userprofile'):
        UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        username_form = UpdateUsernameForm(request.POST, instance=request.user)
        password_form = UpdatePasswordForm(request.user, request.POST)
        preferences_form = UpdatePreferencesForm(request.POST, instance=request.user.userprofile)

        if username_form.is_valid() and password_form.is_valid() and preferences_form.is_valid():
            username_form.save()
            password_form.save()
            preferences_form.save()
            return redirect('user_settings')
    else:
        username_form = UpdateUsernameForm(instance=request.user)
        password_form = UpdatePasswordForm(request.user)
        preferences_form = UpdatePreferencesForm(instance=request.user.userprofile)

    context = {
        'username_form': username_form,
        'password_form': password_form,
        'preferences_form': preferences_form,
        'dark_mode': request.user.userprofile.dark_mode
    }
    return render(request, 'usersettings/user_settings.html', context)


# Create your views here.
