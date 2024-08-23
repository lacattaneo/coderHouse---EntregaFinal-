from django.shortcuts import render, HttpResponse, redirect
from django.template import Template, Context


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def post(request):
    return render(request, 'post.html')

def contact (request):
    return render(request, 'contact.html')

def padre(request):
    return render(request,'padre.html')
