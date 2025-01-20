from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_at') # Controls the columns shown in the admin list view.
    list_filter = ('status', 'created_at', 'published_at') # Adds filters for specific fields in the sidebar.
    search_fields = ('title', 'content') # Enables search functionality for specified fields.
    prepopulated_fields = {'slug': ('title',)} # Automatically generates the slug field based on the title.