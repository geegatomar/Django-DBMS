
from django.shortcuts import (get_object_or_404,
                              render, 
                              HttpResponseRedirect)
from django.http import HttpResponse
from .models import Items, ItemsCart
from .forms import ItemsForm
from django.db.models import Q
from django.contrib.auth.models import User
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
        #results=Items.objects.all().filter(item_name=query).values()
        results=Items.objects.all().raw("Select * from blog_Items where item_name=%s",[query])

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
    context ={}
    obj = get_object_or_404(Items, id = id)
    form = ItemsForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context["form"] = form  
    return render(request, "blog/update.html", context)


def delete_view(request, id):

    context ={}
    obj = get_object_or_404(Items, id = id) 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "blog/delete.html", context)

def buy(request, id):
    obj = get_object_or_404(Items, id = id)
    #cart = ItemsCart.objects.all()
    name = Items.objects.all().filter(id=id).values()
    print(name)
    r=request.user
    print(r)
    cart=ItemsCart(item_id=id, buyer_id=r)
    #cart.buyer_id=request.user
    #cart.item_id=Items.objects.raw("Select id from blog_Items where id=",id)
    #cart.save()
    k=name[0]['author_id']
    context = {}
    context['dataset'] = User.objects.all().filter(id=k).values()

    return render(request, "blog/buy.html", context)

