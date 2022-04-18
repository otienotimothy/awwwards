from django.urls import path

from .views import home, projectDetails, userprofile, uploadProject, loginUser, signupUser, logoutUser, editUserProfile


urlpatterns = [
    path('', home, name='home'),
    path('project/<int:projectId>/', projectDetails, name='projectDetails'),
    path('profile/<str:username>/', userprofile, name='profile'),
    path('profile/edit/', editUserProfile, name='editProfile'),
    path('upload/', uploadProject, name='upload'),
    path('signup/', signupUser, name='signup'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout')
]