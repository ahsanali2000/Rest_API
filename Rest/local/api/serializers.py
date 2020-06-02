from rest_framework import serializers
from local.models import Status

from accounts.api.serializer import UserPublicSerializer


def validate_content(value):
    if len(value) > 10000:
        raise serializers.ValidationError('Content is too long.')
    return value


class StatusSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user']

    def validate_data(self, data):
        content = data.get('content', None)
        image = data.get('image', None)
        if content == "":
            content = None
        if content is None and image is None:
            raise serializers.ValidationError('Content and image is required.')
        return data
