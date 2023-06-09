"""MoversAndPackers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from moverspackers.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('admin_login',admin_login, name="admin_login"),
    path('admin_home',admin_home, name="admin_home"),
    path('logout/',Logout, name="logout"),
    path('add_services',add_services, name="add_services"),
    path('manage_services',manage_services, name="manage_services"),
    path('edit_services/<int:pid>',edit_services, name="edit_services"),
    path('delete_services/<int:pid>',delete_services, name="delete_services"),
    path('services',services, name="services"),
    path('about',about, name="about"),
    path('request_quote',request_quote, name="request_quote"),
    path('new_booking',new_booking, name="new_booking"),
    path('old_booking',old_booking, name="old_booking"),
    path('contact',contact, name="contact"),
    path('unread_queries',unread_queries, name="unread_queries"),
    path('read_queries',read_queries, name="read_queries"),

              ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)   # make sure you write this statement while taking image or any type of media from users

'''
used to give url patterns to the pages created
'''
