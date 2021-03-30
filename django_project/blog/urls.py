from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.about, name='blog-about'),
    path('sell/',views.create_view,name='blog-sell'),
    path('', views.list_view,name='blog-home'),
    path('search/',views.search,name='search'),
    path('<int:id>/itemdetails/', views.detail_view, name='detail'),
    path('<int:id>/update/', views.update_view, name='update'),
    path('<int:id>/delete/', views.delete_view, name='delete'),
    path('<int:id>/buy/', views.buy, name='buy'),
    path('<int:id>/cart/', views.cart, name='cart'),
    path('<int:id>/sale/', views.sale, name='sale'),
]

