from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Post
from api.models import Category
import markdown


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'blurb',
                  'owner', 'image', 'categories']

    def to_representation(self, instance):
        # Convert Markdown to HTML before serializing
        instance.body = markdown.markdown(instance.body)
        instance.blurb = markdown.markdown(instance.blurb)
        return super().to_representation(instance)


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts', 'categories']


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner', 'posts']
