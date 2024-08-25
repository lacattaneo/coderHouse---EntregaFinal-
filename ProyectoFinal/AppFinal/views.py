from django.shortcuts import render, HttpResponse, redirect
from django.template import Template, Context


def index(request):
    return render(request, 'index.html')


def chamame(request):
    return render(request, 'chamame.html')


def ibera(request):
    return render(request, 'ibera.html')

def pesca (request):
    return render(request, 'pesca.html')

def padre(request):
    return render(request,'padre.html')

def carnaval(request):
    return render(request,'carnaval.html')

def yo(request):
    return render(request, 'yo.html')
