from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  # Import timezone

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    date_subscribed = models.DateTimeField(default=timezone.now)  # Set default value

    def __str__(self):
        return self.email
