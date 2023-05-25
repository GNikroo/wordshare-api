from django.shortcuts import render
from .models import FeaturedPost
from .serializers import FeaturedPostSerializer
from rest_framework import generics, permissions, filters
from ws_api.permissions import IsOwnerOrReadOnly
from django.utils import timezone


class Featured(generics.ListAPIView):
    serializer_class = FeaturedPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = FeaturedPost.objects.all()
    filter_backends = [
        filters.SearchFilter,
    ]
    search_fields = [
        'owner__username',
        'title',
        'featured',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FeaturedDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FeaturedPostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = FeaturedPost.objects.all()
