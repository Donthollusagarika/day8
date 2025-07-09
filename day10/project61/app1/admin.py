from django.contrib import admin

# Register your models here.
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
]
