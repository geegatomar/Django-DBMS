
from django.shortcuts import (get_object_or_404,
                              render, 
                              HttpResponseRedirect)
from django.http import HttpResponse
from .models import Items
from .forms import ItemsForm
from django.db.models import Q
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
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
        #esults=Items.objects.all().raw("Select * from blog_Items where item_name="+query+";")
    return render(request,"blog/search.html",{'query':query,'results':results})

# pass id attribute from urls
def detail_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    context["data"] = Items.objects.get(id = id)
          
    return render(request, "blog/itemdetails.html", context)

def update_view(request, id):
    # dictionary for initial data with 
    # field names as keys
    context ={}
  
    # fetch the object related to passed id
    obj = get_object_or_404(Items, id = id)
  
    # pass the object as instance in form
    form = ItemsForm(request.POST or None, instance = obj)
  
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
  
    # add form dictionary to context
    context["form"] = form
  
    return render(request, "blog/update.html", context)