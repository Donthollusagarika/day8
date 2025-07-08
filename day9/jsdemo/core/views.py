from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

Step 4a: Set Up URL Routing
