from django.shortcuts import render
from .models import Post, Subscriber  # Import the Post and Subscriber models

def home(request):
    posts = Post.objects.all()  # Retrieve all posts using the Post model
    return render(request, 'blogposts/home.html', {'posts': posts})

def about(request):
    return render(request, 'blogposts/about.html')

def contacts(request):
    return render(request, 'blogposts/contacts.html')

def subscriber_list(request):
    subscribers = Subscriber.objects.all()  # Retrieve all subscribers using the Subscriber model
    return render(request, 'blogposts/subscriber_list.html', {'subscribers': subscribers})
