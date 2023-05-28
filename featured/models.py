from django.db import models
from django.utils import timezone
from posts.models import Post


class FeaturedPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_current_featured_post(cls):
        today = timezone.now().date()
        try:
            featured_post = cls.objects.get(created_at__date=today)
        except cls.DoesNotExist:
            featured_post = None
        return featured_post

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'featured: {self.post.title}'
