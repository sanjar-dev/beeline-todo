"""beelinetodos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('test/', test, name="test"),
    path('add-todo/', add_todo, name="add-todo"),
    path('delete-todo/<id>/', delete_todo, name="delete-todo"),
    path('mark-todo/<id>/', mark_todo, name="mark-todo"),
    path('toggle-todo/<id>/', toggle_todo, name="toggle-todo"),
    path('meetings/', meetings, name="meetings"),
    path('add-meeting/', add_meeting, name="add-meeting"),
    path('delete-meeting/<id>/', delete_meeting, name="delete-meeting"),
    path('mark-meeting/<id>/', mark_meeting, name="mark-meeting"),
    path('habits/', habits, name="habits"),
    path('add_habit/', add_habit, name="add-habit"),
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
