from django.shortcuts import render
from django.http  import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    
    return render(request,'art/index.html')

def landing(request):
    
    return render(request,'art/home.html')

def about(request):
    return render(request,'art/about.html')
