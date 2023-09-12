from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    Artist = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='artpieces/')
    starting_bid = models.IntegerField(blank=True, null=True)
    # tags = models.ManyToManyField(tags)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def save(self):
        super().save()

        # img = Image.open(self.image.path)
        # if img.height < 700 or img.width < 700:
        #     output_size = (700, 700)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    Artist = models.ForeignKey(User, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    
class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
