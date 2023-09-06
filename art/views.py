from django.shortcuts import render
from django.http  import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
def home(request):
    
    return render(request,'art/index.html')

class PostListView(ListView):
    model = Post
    template_name = 'art/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

def landing(request):
    
    return render(request,'art/home.html')

def about(request):
    return render(request,'art/about.html')
