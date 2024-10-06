from django.contrib import admin
from django.urls import path, include

from apps.project.views.project_views import ProjectApi
from apps.tasks import apps

urlpatterns = [
    path('projects/', ProjectApi.as_view(), name='project'),
]
