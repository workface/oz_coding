"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.shortcuts import render
from django.http import Http404
from fake_db import user_db

db = user_db

def user_list(request):
    users = [{'id': key, 'name': value['이름']} for key, value in db.items()]
    return render(request, template_name='user_list.html', context={'users': users})

def user_info(request, user_id):
    if user_id < 1 or user_id > 5 :
        raise Http404('Users not found')
    user = db[user_id]
    context = {'user': user}
    return render(request, 'user_info.html', context)








urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', user_list),
    path('users/<int:user_id>/', user_info),
]
