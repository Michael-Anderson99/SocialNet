from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at my sites homepage")

def hello(request):
    return HttpResponse("helooooo")