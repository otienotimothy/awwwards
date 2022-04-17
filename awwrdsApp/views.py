from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile, Project
from .forms import UserRegistrationForm, LoginUserForm


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
                userProfile = Profile(user=user)
                userProfile.save()
                login(request, user)
                return redirect('home')
            

    form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'signup.html', context)

def loginUser(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'].lower()
            password = form.cleaned_data['password']
            try:
                user_exist = User.objects.get(username=username)
                if user_exist:
                    user = authenticate(
                        request, username=username, password=password)
                    if user:
                        login(request, user)
                        return redirect('home')
                    else:
                        messages.error(request, 'Invalid username or password')
            except:
                messages.error(request, 'User does not exist, sign-up')

    form = LoginUserForm()
    context = {'form': form}
    return render(request, 'login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect(loginUser)

def home(request):

    if Project.objects.all().exists():
        projects = Project.objects.all()
        context = {'projects': projects}
        return render(request, 'index.html', context)
    else:
        return render(request, '404.html')

def projectDetails(request, projectName):
    try:
        project = Project.objects.get(projectName = projectName)
        context = {'project': project}
        return render(request, 'project.html', context)
    except:
        return render(request, '404.html')

def userprofile(request, username):

    if request.user.username != username:
        logout(request)
        redirect(loginUser)

    try:
        userProfile = User.objects.get(username=username)
    except:
        messages.error(
            request, 'An Error Occured while trying to load your Profile')

    context = {'userProfile': userProfile}
    return render(request, 'profile.html', context)

def uploadProject(request):
    return render(request, 'upload.html')