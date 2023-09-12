from django.shortcuts import render, get_object_or_404, redirect
from django.http  import HttpResponse
from django.urls import reverse_lazy
from .models import Post, Conversation, Message, Comment
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.
def home(request):
    posts = Post.objects.all()
    # count = Post.objects.all().count()
    # context={'count': count}
    return render(request,'art/index.html', {"posts": posts})

class PostListView(ListView):
    model = Post
    template_name = 'art/corey_home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.Artist = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Artist:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Artist:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'starting_bid']

    def form_valid(self, form):
        form.instance.Artist = self.request.user
        return super().form_valid(form)
    
class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'art/add_comment.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('post-home')

def landing(request):
    
    return render(request,'art/home.html')

def about(request):
    return render(request,'art/about.html')

# conversations views.py


def get_messages(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id)
    messages = Message.objects.filter(conversation=conversation).order_by('timestamp')
    return render(request, 'art/post_detail.html', {'messages': messages, 'conversation': conversation})

def send_message(request, conversation_id):
    if request.method == 'POST':
        conversation = get_object_or_404(Conversation, id=conversation_id)
        sender = request.user
        content = request.POST.get('content', '')

        if content:
            message = Message(conversation=conversation, sender=sender, content=content)
            message.save()

    return redirect('get_messages', conversation_id=conversation_id)
