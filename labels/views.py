from rest_framework import generics, permissions
from ws_api.permissions import IsOwnerOrReadOnly
from .models import Label
from .serializers import LabelSerializer, LabelDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend


class LabelList(generics.ListCreateAPIView):
    serializer_class = LabelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Label.objects.all()
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'post__id',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LabelDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LabelDetailSerializer
    queryset = Label.objects.all()
