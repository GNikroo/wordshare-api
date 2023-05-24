from rest_framework import serializers
from .models import Label


class LabelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Label
        fields = [
            'id', 'owner', 'is_owner', 'post',
            'created_at', 'updated_at', 'content'
        ]


class LabelDetailSerializer(LabelSerializer):
    post = serializers.ReadOnlyField(source='post.id')
