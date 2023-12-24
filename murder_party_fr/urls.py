"""
URL configuration for murder_party_fr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from murder import views

urlpatterns = [
    path('', views.home, name='home'),
    path('murder-party-team-building', views.teambuilding, name='teambuilding'),
    path('murder-party-amis-famille', views.friends, name='friends'),
    path('comment-organiser-une-murder-party', views.how_to, name='how_to'),
    path('qu-est-ce-qu-une-murder-party', views.what, name='what'),
    path('murder-party-blog', views.blog, name='blog'),
    path('murder-party-paris', views.murder_party_paris, name='murder-party-paris'),
    path('murder-party-lille', views.murder_party_lille, name='murder-party-lille'),
    path('murder-party-villes-france', views.murder_party_france, name='murder-party-france'),
    path('murder-party/redrock-saloon', views.scenario_page, name='scenario_page'),
    path('murder-party/sherlock-party', views.scenario_page, name='scenario_page'),
    path('admin/', admin.site.urls),
]

urlpatterns += staticfiles_urlpatterns()
