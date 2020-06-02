from rest_framework import serializers
from local.models import Status
from rest_framework.reverse import reverse as api_reverse

from accounts.api.serializer import UserPublicSerializer


def validate_content(value):
    if len(value) > 10000:
        raise serializers.ValidationError('Content is too long.')
    return value


class StatusSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    uri=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image',
            'uri'
        ]
        read_only_fields = ['user']
    def get_uri(self,obj):
        request = self.context.get('request')
        return api_reverse('api-local:details',kwargs={'id':obj.id}, request=request)
    def validate_data(self, data):
        content = data.get('content', None)
        image = data.get('image', None)
        if content == "":
            content = None
        if content is None and image is None:
            raise serializers.ValidationError('Content and image is required.')
        return data
