from django.contrib import admin
from localizador.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
