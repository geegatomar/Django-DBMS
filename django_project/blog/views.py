from django.shortcuts import render
from django.http import HttpResponse
from .models import Items
from .forms import ItemsForm
from django.db.models import Q
# Create your views here.


def home(request):
    # render takes 2 arguments; the request, and the string of the path of the html file to render
    return render(request, 'home.html')


def about(request):
    return render(request, 'blog/about.html')


def create_view(request): 
    context ={} 

    form = ItemsForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
          
    context['form']= form 
    return render(request,'blog/sell.html',context)

def list_view(request):
    context ={}
    context["dataset"] = Items.objects.raw('Select * from blog_Items')       
    return render(request, "blog/home.html", context)

def search(request):
    if request.method=="GET":
        query=request.GET.get('search')
        print(query)
        results=Items.objects.all().filter(item_name=query)
    return render(request,"blog/search.html",{'query':query,'results':results})