from shorter.models import Shorter
from rest_framework import serializers


class ShorterSerializer(serializers.ModelSerializer):
    original_url = serializers.URLField(required=True)
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = Shorter
        fields = ('original_url', 'short_url')

    def get_short_url(self, obj):
        request = self.context.get('request')
        return obj.get_short_url(request)
