
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
    
    return HttpResponse("hello,Django!())
