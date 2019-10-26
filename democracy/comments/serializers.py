from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['uuid', 'user_uuid', 'parent_uuid', 'target_uuid', 'content', 'created_at', 'updated_at', ]

    def create(self):
        return Comment(**validated_data)