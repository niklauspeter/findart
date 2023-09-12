from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'write down your bid amount': forms.Textarea(attrs={'class': 'form-control'}),
        }