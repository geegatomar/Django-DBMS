
from django.shortcuts import (get_object_or_404,
                              render, 
                              HttpResponseRedirect)
from django.http import HttpResponse,  HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import Items, ItemsCart
from .forms import ItemsForm,ItemsCartForm
from django_project.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail  

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'blog/about.html')


def create_view(request): 
    context ={} 
    form = ItemsForm(request.POST or None) 
    if form.is_valid(): 
        item = form.save(commit = False)
        item.author = request.user   
        item.save()   
        return HttpResponseRedirect("/")        
    context['form']= form 
    return render(request,'blog/sell.html',context)

def list_view(request):
    context ={}
    context["dataset"] = Items.objects.raw('Select * from blog_Items')       
    return render(request, "blog/home.html", context)

def search(request):
    if request.method=="GET":
        query=request.GET.get('search')
        results=Items.objects.all().filter(item_name=query).values()
        #results=Items.objects.all().raw("Select * from blog_Items where item_name='%s'",[query])
        print(results)

    return render(request,"blog/search.html",{'query':query,'results':results})

def detail_view(request, id):   
    context ={}
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
    name = Items.objects.all().filter(id=id).values()
    k=name[0]['author_id']
    m=name[0]['item_name']
    context = {}
    context['dataset'] = User.objects.all().filter(id=k).values()
    con = User.objects.all().filter(id=k).values()
    print(con)
    c=con[0]['email']
    
    form = ItemsCartForm(request.POST or None) 
    if form.is_valid(): 
        cart=ItemsCart.objects.get_or_create(item_id=Items.objects.get(id=id), buyer_id=request.user)
        update=Items.objects.filter(id=id).update(status=0)
        subject = 'There is a person interested in buying your item.'
        message = f'Hi {request.user}  wants to buy the item {m} which you put up for sale. If you are not contacted by them here are their details: email: {request.user.email}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [c]
        send_mail( subject, message, email_from, recipient_list )      
        return HttpResponseRedirect("/")      
    return render(request, "blog/buy.html", context)

def cart(request, id):
    context ={}
    context["dataset"] = ItemsCart.objects.all().filter(buyer_id=id)     
    return render(request, "blog/cart.html",context)

def sale(request, id):
    context ={}
    context["dataset"] = Items.objects.raw('Select * from blog_Items')       
    return render(request, "blog/sale.html", context)


