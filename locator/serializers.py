from rest_framework import serializers
from locator.models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'slug', 'status', 'published', 'created_at', 'updated_at', 'image1', 'image2', 'image3', 'author']

    author = serializers.StringRelatedField()
    published = serializers.BooleanField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def validated_title(self, value):
        title = value
        if len(title) < 5:
            raise serializers.ValidationError('Mais do que cinco')

        return title

    def validate(self, attrs):
        superValidate = super().validate(attrs)
        errors = []

        title = attrs.get('title')
        description = attrs.get('description')

        if title == description:
            errors['title'].append('Nao pode ser igual')
            errors['description'].append('Nao pode ser igual')

        if errors:
            raise serializers.ValidationError(errors)

        return superValidate
