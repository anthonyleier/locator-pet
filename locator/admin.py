from django.contrib import admin
from locator.models import Post, Profile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published', 'found', 'user', 'created_at', 'updated_at']
    list_display_links = ['id', 'title']
    list_filter = ['user', 'published', 'found']
    search_fields = ['id', 'title', 'description']
    list_per_page = 20
    list_editable = ['published', 'found']
    ordering = ['-id']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'phone']
    search_fields = ['id', 'user', 'phone']
    list_per_page = 20
    ordering = ['-id']
