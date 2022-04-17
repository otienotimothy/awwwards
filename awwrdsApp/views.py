from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm


# Create your views here.

def signupUser(request):

    if request.user.is_authenticated:
        redirect('home')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        user = form.save(commit=False)
        if form.is_valid():
            if User.objects.filter(username=user.username.lower()).exists():
                messages.error(
                    request, f'A User with the username, {user.username}, Already exists')
            elif User.objects.filter(email=user.email.lower()).exists():
                messages.error(
                    request, f'A user with the email, {user.email}, Already exists')
            else:
                user.email = user.email.lower()
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect('home')
            

    form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'signup.html', context)

def loginUser(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'index.html')

def projectDetails(request):
    return render(request, 'project.html')

def userprofile(request):
    return render(request, 'profile.html')

def uploadProject(request):
    return render(request, 'upload.html')