from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('sell/',views.create_view,name='blog-sell'),
    path('', views.list_view,name='blog-home'),
    path('search/',views.search,name='search'),
    path('<int:id>/itemdetails/', views.detail_view, name='detail'),
    path('<int:id>/update/', views.update_view, name='update'),
]
