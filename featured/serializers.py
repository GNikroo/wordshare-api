from rest_framework import serializers
from featured.models import FeaturedPost


class FeaturedPostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = FeaturedPost
        fields = [
            'id', 'owner', 'is_owner', 'post'
        ]
