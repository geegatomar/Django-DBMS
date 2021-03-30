
from django.shortcuts import (get_object_or_404,
                              render, 
                              HttpResponseRedirect)
from django.http import HttpResponse,  HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from .models import Items, ItemsCart
from .forms import ItemsForm,ItemsCartForm
from django.db.models import Q
from django.contrib.auth.models import User

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
    name = Items.objects.all().filter(id=id).values()
    k=name[0]['author_id']
    context = {}
    context['dataset'] = User.objects.all().filter(id=k).values()
    form = ItemsCartForm(request.POST or None) 
    if form.is_valid(): 
        cart=ItemsCart.objects.get_or_create(item_id=Items.objects.get(id=id), buyer_id=request.user)
        update=Items.objects.filter(id=id).update(status=0)
            
    return render(request, "blog/buy.html", context)

def cart(request, id):
    context ={}
    context["dataset"] = ItemsCart.objects.all().filter(buyer_id=id)     
    return render(request, "blog/cart.html",context)

def sale(request, id):
    context ={}
    context["dataset"] = Items.objects.raw('Select * from blog_Items')       
    return render(request, "blog/sale.html", context)


# def contact(request):
#     from blog.mailer import send_mail

#     if request.method == "POST":
#         form = ContactUsForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             query = form.cleaned_data['query']
#             mail_sent = send_mail(name,email,query)
#             if mail_sent:
#                 messages.success(request, 'Your query has been successfully sent')
#             else:
#                 messages.error(request, 'Query submission unsuccessful, try again or mail help@plus-robotics.com')
#         else:
#             messages.error(request, 'Query Submission Unsuccessful, try again or mail help@plus-robotics.com')
#         return HttpResponseRedirect(reverse('contact'))
#     else:
#         form = ContactUsForm()
#         context = { 'form' : form }

#     return render(request, 'contact.html', context=context) 