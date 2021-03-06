from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm, UserChangeForm, PasswordChangeForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
import re

def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        reverse('home')  # TODO: go to profile
                    )
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            if re.search(username, password):
                messages.success(
                    request,
                    "fail password can not include your name"
                )
                return render(request, 'accounts/sign_up.html', {'form': form})
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            return HttpResponseRedirect(reverse('home'))  # TODO: go to profile
    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))

@login_required
def profile_detail(request):
    profile = request.user.profile
    return render(request, 'accounts/detail.html', {'profile':profile})

@login_required
def profile_edit(request):
    original_profile = request.user.profile
    form = ProfileForm(instance = original_profile)
    if request.method =='POST':
        form = ProfileForm(instance = original_profile,data = request.POST,
            files = request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'save change!')
            return HttpResponseRedirect(reverse('accounts:profile_detail'))
    return render(request, "accounts/edit.html",{'form':form})

# refer https://anitanad.wordpress.com/2019/03/11/django-tips-9-how-to-create-a-change-password-view/
@login_required
def change_password(request):
    profile = request.user.profile
    form = PasswordChangeForm(request.user, request.POST)
    if request.method == 'POST':
        if form.is_valid():
            password=form.cleaned_data['new_password1']
            if re.search(profile.first_name, password):
                messages.success(
                    request,
                    "fail, password can not include your first name"
                )
                return render(request, 'accounts/sign_up.html', {'form': form})


            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect(reverse('accounts:profile_detail'))

    return render(request, "accounts/change_password.html",{'form':form})
