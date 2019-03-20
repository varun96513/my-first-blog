from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def html1(request):
    page1 = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/html1.html', {'page1': page1})