# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('contacts/', views.contacts, name='contacts'),  # Contacts page
    path('subscribers/', views.subscriber_list, name='subscriber_list'),  # Subscriber list
]
