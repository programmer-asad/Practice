from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def email(request):
    return HttpResponse("Here is email management system")