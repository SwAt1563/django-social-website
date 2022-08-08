from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from account.forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib import messages
# Create your views here.


class LoginView(views.LoginView):
    pass


class LogoutView(views.LogoutView):
    pass


class PasswordChangeView(views.PasswordChangeView):
    pass


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    pass


# For enter the email and send the request to it
class PasswordResetView(views.PasswordResetView):
    pass


# For tell you the message to the email is done
class PasswordResetDoneView(views.PasswordResetDoneView):
    pass


# When make response from email to enter new password
class PasswordResetConfirmView(views.PasswordResetConfirmView):
    pass


# when the change is done of rest password
class PasswordResetCompleteView(views.PasswordResetCompleteView):
    pass


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


@login_required
def dashboard(request):

    return render(request, 'account/dashboard.html',
                  {
                      'section': 'dashboard',
                  }
                  )


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Success Update')
        else:
            messages.error(request, 'Error Updating')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
