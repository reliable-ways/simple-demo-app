from django.shortcuts import render, get_object_or_404
from .models import Post

from django.core.paginator import Paginator

def post_list(request):
    tag = request.GET.get('tag')
    posts = Post.objects.filter(status='published').order_by('-published_at')
    if tag:
        posts = posts.filter(tags__name=tag)

    # Paginate posts (10 per page)
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {'posts': page_obj})


def post_detail(request, pk, slug):
    post = get_object_or_404(Post, pk=pk, slug=slug, status='published')
    post.views += 1  # Increment the views count
    post.save()  # Save the updated view count to the database
    return render(request, 'post_detail.html', {'post': post})