from django.contrib import admin
from locator.models import Post, Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published', 'found', 'author', 'created_at']
    list_display_links = ['id', 'title', 'created_at']
    list_filter = ['author', 'published', 'found']
    search_fields = ['id', 'title', 'description']
    list_per_page = 10
    list_editable = ['published']
    ordering = ['-id']
    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'phone', 'address']
    search_fields = ['id', 'phone', 'address']
    list_per_page = 10
    ordering = ['-id']
