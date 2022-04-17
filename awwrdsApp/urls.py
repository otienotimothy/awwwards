from django.urls import path

from .views import home, projectDetails, userprofile, uploadProject, loginUser, signupUser


urlpatterns = [
    path('', home, name='home'),
    path('project/', projectDetails, name='projectDetails'),
    path('profile/', userprofile, name='profile'),
    path('upload/', uploadProject, name='upload'),
    path('signup/', signupUser, name='signup'),
    path('login/', loginUser, name='login')
]