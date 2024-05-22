from django.contrib import admin
from .models import Post, Subscriber  # Adjusted import statement

class PostAdmin(admin.ModelAdmin):  # Adjusted class name to follow conventions
    list_display = ('title', 'created_at', 'author')  # Adjusted field name to follow conventions
    search_fields = ('title', 'created_at', 'author')
    list_filter = ('created_at', 'author')

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')
    search_fields = ('email', 'name')
    list_filter = ('email',)

# Register your models here.
admin.site.register(Post, PostAdmin)  # Adjusted model name to follow conventions
admin.site.register(Subscriber, SubscriberAdmin)
