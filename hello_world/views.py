from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Ok so so far i do seem to understand the concept of how django works. i is liking this.")
