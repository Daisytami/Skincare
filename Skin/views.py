from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def Skin(request):
    return HttpResponse("Skincare is Hereditary")

def base(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def shop(request):
    template = loader.get_template('shop.html')
    return HttpResponse(template.render())
def services(request):
    template = loader.get_template('services.html')
    return HttpResponse(template.render())
def body(request):
    template = loader.get_template('body.html')
    return HttpResponse(template.render())


# Create your views here.
