from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, this is the products index page.")
