from django.urls import path
from . import views
urlpatterns = [
   path('insert_student/',views.insert_employee,name='insert_student'),
    # other paths as needed
]
