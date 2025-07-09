from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def  home(request):
    temp=loader.get_template('home.html')
    return HttpResponse(temp.render())
from django.urls import path
from . import views
urlpatterns = [
   path('',views.home, name='home'),
	]
