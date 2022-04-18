from django.urls import path

from .views import home, projectDetails, userprofile, uploadProject, loginUser, signupUser, logoutUser, editUserProfile, rateProject


urlpatterns = [
    path('', home, name='home'),
    path('project/<int:projectId>/', projectDetails, name='projectDetails'),
    path('profile/<str:username>/', userprofile, name='profile'),
    path('profile/<str:username>/edit/', editUserProfile, name='editProfile'),
    path('upload/', uploadProject, name='upload'),
    path('signup/', signupUser, name='signup'),
    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('rate/<int:projectId>/', rateProject, name='rate')
]