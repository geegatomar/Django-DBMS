from django.shortcuts import render
from django.http import HttpResponse
from .models import Items
from .forms import ItemsForm

# Create your views here.


def home(request):
    # render takes 2 arguments; the request, and the string of the path of the html file to render
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')


def create_view(request): 
    context ={} 

    form = ItemsForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
          
    context['form']= form 
    return render(request,'blog/sell.html',context)
