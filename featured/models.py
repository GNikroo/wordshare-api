import random
from datetime import timedelta

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from posts.models import Post


def generate_random_date():
    random_days = random.randint(1, 30)
    random_date = timezone.now().date() - timedelta(days=random_days)
    return random_date


class FeaturedPost(models.Model):
    featured_post = models.OneToOneField(Post, on_delete=models.CASCADE)
    featured_date = models.DateField(default=generate_random_date)

    def __str__(self):
        return f'featured: {self.post.title}'
