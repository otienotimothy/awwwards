from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def projectDetails(request):
    return render(request, 'project.html')

def userprofile(request):
    return render(request, 'profile.html')