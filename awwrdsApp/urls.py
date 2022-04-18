from django.urls import path

from .views import home, projectDetails, userprofile, uploadProject, loginUser, signupUser, logoutUser


urlpatterns = [
    path('', home, name='home'),
    path('project/', projectDetails, name='projectDetails'),
    path('profile/<str:username>/', userprofile, name='profile'),
    path('upload/', uploadProject, name='upload'),
    path('signup/', signupUser, name='signup'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout')
]