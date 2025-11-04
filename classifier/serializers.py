from rest_framework import serializers
from .models import UploadedImage

class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ['id', 'image', 'is_garbage', 'created_at']
        read_only_fields = ['is_garbage', 'created_at']
