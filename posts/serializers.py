from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'username', 'created_at']
    
    def get_username(self, obj):
        if obj.is_anonymous:
            return "Anonymous"
        return obj.user.username if obj.user else "Unknown"

