from multiprocessing import context
from django.shortcuts import render

from .forms import UserRegistrationForm


# Create your views here.

def signupUser(request):

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