from rest_framework import serializers
from Blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'author','excerpt', 'content','status')