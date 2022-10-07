from django.contrib import admin
from locator.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
