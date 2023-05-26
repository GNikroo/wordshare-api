from rest_framework import serializers
from posts.serializers import PostSerializer
from .models import FeaturedPost


class FeaturedPostSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = FeaturedPost
        fields = ['post']
