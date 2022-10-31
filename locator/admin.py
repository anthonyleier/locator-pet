from django.contrib import admin
from locator.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at', 'published', 'author']
    list_display_links = ['id', 'title', 'created_at']
    list_filter = ['author', 'published']
    search_fields = ['id', 'title', 'description']
    list_per_page = 10
    list_editable = ['published']
    ordering = ['-id']
    prepopulated_fields = {
        'slug': ['title']
    }
