from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'static_handler.html')

def index(request):
    return render(request, 'index.html')
    
