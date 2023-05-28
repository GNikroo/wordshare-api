from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import FeaturedPost
from .serializers import FeaturedPostSerializer
from posts.models import Post
from django.utils import timezone
from datetime import timedelta
import random


class RandomFeaturedPost(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FeaturedPostSerializer

    def get_object(self):
        featured_post = FeaturedPost.get_current_featured_post()

        if featured_post is None:
            random_post = random.choice(Post.objects.all())
            featured_post = FeaturedPost.objects.create(post=random_post)
        else:
            current_time = timezone.now()
            time_difference = current_time - featured_post.created_at
            if time_difference >= timedelta(days=1):
                random_post = random.choice(Post.objects.all())
                featured_post.post = random_post
                featured_post.save()

        return featured_post
