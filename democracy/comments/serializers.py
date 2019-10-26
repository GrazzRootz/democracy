from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['uuid', 'target_uuid', 'content', 'created_at', 'updated_at', ]
    
    def create(self, validated_data):
        raise NotImplementedError("POSTING COMMENTS IS NOT SUPPORTED! >:( ")