from rest_framework import serializers
from .models import Box


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ("box_id", "")