from django.shortcuts import render
from .models import Post

def blog_list(request):
    tag = request.GET.get('tag')  # Get tag from query parameters
    if tag:
        posts = Post.objects.filter(tags__name__in=[tag])
    else:
        posts = Post.objects.all()
    return render(request, 'blog_list.html', {'posts': posts})