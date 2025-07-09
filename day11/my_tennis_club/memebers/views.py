from django.http import HttpResponse
from django.template import loader

# Create your views here.

def memebers(request):
template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
