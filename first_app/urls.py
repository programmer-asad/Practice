from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_page),
    path('home/', views.home_page),
    path('about/', views.about_page),
    path('contact/', views.contact_page),
    path('orders/', views.order_page),
]