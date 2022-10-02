from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# views (classes) defined here


def hello(request):
    return HttpResponse("Hello World")


def show_details(request, id):
    return HttpResponse(f"Job detail page {id}")
