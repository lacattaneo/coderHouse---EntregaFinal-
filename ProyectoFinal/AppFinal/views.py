from django.shortcuts import render, HttpResponse, redirect
from django.template import Template, Context


def index(request):
    return render(request, 'index.html')


def aboutCorrientes(request):
    return render(request, 'appFinal/about.html')


def exploraCorrientes(request):
    return render(request, 'ppFinal/post.html')
