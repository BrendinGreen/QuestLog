"""QuestLog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from Log import views as log_views

urlpatterns = [

    path('games/', log_views.games, name='home'),
    path('locations/', log_views.locations),
    path('skills/', log_views.skills),
    path('objectives/', log_views.objectives),

    path('signup/', log_views.signup),
    path('admin/', admin.site.urls),
    path('login/', auth_views.login),
    path('logout/', auth_views.logout),
]
