from django.urls import path
from . import views

urlpatterns = [
    path('memebers/', views.memebers, name='memebers'),
]
