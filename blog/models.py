from django.db import models

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]
    
    title = models.CharField(max_length=200) # Stores the title of the blog post.
    slug = models.SlugField(max_length=200, unique=True) # Generates a URL-friendly identifier for the post, based on the title.
    content = models.TextField() # Stores the main content of the post.
    author = models.CharField(max_length=100) # Specifies the author’s name.
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft') # Indicates whether the post is published or still in draft mode.
    created_at = models.DateTimeField(auto_now_add=True) # Automatically records when the post was created.
    published_at = models.DateTimeField(blank=False, null=True) # Records when the post was published (optional).
    views = models.PositiveIntegerField(default=0)  # Field to track views

    class Meta:
        # attribute ensures that posts are sorted by publication date in descending order (most recent first).
        ordering = ['-published_at']
        
    def __str__(self):
        return self.title