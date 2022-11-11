from rest_framework import serializers
from locator.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'slug', 'status', 'published', 'created_at', 'updated_at', 'image1', 'image2', 'image3', 'author']

    author = serializers.StringRelatedField()
    published = serializers.BooleanField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
