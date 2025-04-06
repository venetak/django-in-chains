from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. No tracks yet.")

def tulip(request):
    return HttpResponse("(\^/)")

def rose(request):
    return HttpResponse("((o))")