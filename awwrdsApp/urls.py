from django.urls import path

from .views import home, projectDetails


urlpatterns = [
    path('', home, name='home'),
    path('project', projectDetails, name='projectDetails')
]