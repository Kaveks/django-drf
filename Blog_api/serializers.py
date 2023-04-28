from rest_framework import serializers
from Blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'image','title','slug','author','excerpt', 'content','status')