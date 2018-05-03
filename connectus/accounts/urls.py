"""connectus URL Configuration

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
from django.urls import path, include,re_path
from django.contrib.auth import views as auth_views
from . import views


app_name_ = 'accounts'

urlpatterns = [

   
    path('', auth_views.login, {'template_name':'accounts/starter.html'}, name="login"),
    path('logout/', auth_views.logout, {'template_name':'accounts/logout.html'}, name="logout"),
    path('register/', views.register,  name="register"),
    path('searchjobs/', views.jobsfinder,  name="jobs-search"),
    path('profile/', views.profile,  name="profile"),
    path('update/', views.update_profile,  name="update-profile"),
    re_path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends'),
    re_path(r'^users/$', views.view_profile, name='view_profile'),
    re_path(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
   
]
