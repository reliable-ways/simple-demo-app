from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

class Post(models.Model):
    STATUS_CLOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(max_length=200) # Stores the title of the blog post.
    slug = models.SlugField(max_length=200, unique=True) # Generates a URL-friendly identifier for the post, based on the title.
    content = models.TextField() # Stores the main content of the post.
    author = models.CharField(max_length=100) # Specifies the author’s name.
    status = models.CharField(max_length=10, choices=STATUS_CLOICES, default='draft') # Indicates whether the post is published or still in draft mode.
    created_at = models.DateTimeField(auto_now_add=True) # Automatically records when the post was created.
    published_at = models.DateTimeField(blank=True, null=True) # Records when the post was published (optional).
    tags = TaggableManager()  # Add the tagging functionality

    class Meta:
        # attribute ensures that posts are sorted by publication date in descending order (most recent first).
        ordering = ['-published_at']
        
    def __str__(self):
        return self.title