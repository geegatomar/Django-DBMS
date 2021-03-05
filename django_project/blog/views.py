from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # render takes 2 arguments; the request, and the string of the path of the html file to render
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')
