from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import FeaturedPost
from .serializers import FeaturedPostSerializer
from posts.models import Post
from django.utils import timezone
import random


class RandomFeaturedPost(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FeaturedPostSerializer

    def get_object(self):
        featured_post = FeaturedPost.objects.first()

        if featured_post:
            if timezone.now() - featured_post.created_at > timezone.timedelta(days=1):  # noqa
                random_post = random.choice(Post.objects.all())
                featured_post.post = random_post
                featured_post.save()
        else:
            random_post = random.choice(Post.objects.all())
            featured_post = FeaturedPost.objects.create(post=random_post)

        return featured_post
