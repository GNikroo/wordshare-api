from django.db import models
from django.utils import timezone
from posts.models import Post


class FeaturedPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'featured: {self.post.title}'
