from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_page(request):
    return render(request, 'index.html')


def home_page(request):
    return render(request, 'home.html')


def about_page(request):
    return render(request, 'about.html')


def contact_page(request):
    return render(request, 'contact.html')


def order_page(request):
    return render(request, 'order.html')