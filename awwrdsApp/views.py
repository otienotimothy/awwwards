from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg
from .models import Profile, Project, Rating
from .forms import UserRegistrationForm, LoginUserForm, EditProfileForm, UploadProjectForm, ReviewProjectForm


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

def projectDetails(request, projectId):
    form = ReviewProjectForm()
    try:
        project = Project.objects.get(pk = projectId)
        designAvg = project.project_rating.all().aggregate(Avg('design'))
        print(designAvg)
        context = {'project': project, 'form': form}
        return render(request, 'project.html', context)
    except:
        return render(request, '404.html')

@login_required(login_url='login')
def userprofile(request, username):

    form = EditProfileForm()

    if request.user.username != username:
        logout(request)
        return redirect(loginUser)

    try:
        userProfile = User.objects.get(username=username)
        context = {'userProfile': userProfile, 'form': form}
        return render(request, 'profile.html', context)
    except:
        messages.error(
            request, 'An Error Occured while trying to load your Profile')
        return render(request, '404.html')
    
@login_required(login_url='login')
def uploadProject(request):

    if (not request.user.is_authenticated):
        return redirect('login')


    if request.method == 'POST':
        form = UploadProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.projectBy_id = request.user.id
            project.save()
            # Add Default Rating to the Project
            rating = Rating()
            rating.design = 5.0
            rating.usability = 5.0
            rating.content = 5.0
            rating.project_id = project.id
            rating.user = request.user.id
            rating.save()
            messages.success(request, 'Project Uploaded Successfully')
        else:
            messages.error(
                'An Error Occurred while trying to Upload your project')

    form = UploadProjectForm()
    context = {'form': form}
    return render(request, 'upload.html', context)

@login_required(login_url='login')
def rateProject(request, projectId):

    if request.method == 'POST':
        form = ReviewProjectForm(request.POST)
        if form.is_valid:
            rating = form.save(commit=False)
            rating.project_id = projectId
            rating.user_id = request.user.id
            rating.save()
            messages.success(request, 'Your Review has been saved Successfully')
            return redirect(projectDetails, projectId = projectId)
            
    else:
        return render(request, '404.html')
