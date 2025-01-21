from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from .models import Post


def blog_list(request):
    tag = request.GET.get('tag')  # Get tag from query parameters
    if tag:
        posts = Post.objects.filter(tags__name__in=[tag])
    else:
        posts = Post.objects.all()
    return render(request, 'blog_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.views += 1  # Increment the views count
    post.save()  # Save the updated view count to the database
    return render(request, 'post_detail.html', {'post': post})