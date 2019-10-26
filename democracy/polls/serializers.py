from rest_framework import serializers
from .models import Question, Choice

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'uuid', 'user_uuid', 'target_uuid', 'title', 'created_at', 'updated_at',     
        ]

    def create(self, validated_data):
        return Question(**validated_data)

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'uuid', 'question', 'choice_text', 'votes', 'created_at', 
        ]

    def create(self, validated_data):
        return Choice(**validated_data)

class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer()

    class Meta:
        model = Question
        fields = [
            'uuid', 'user_uuid', 'target_uuid', 'choices', 'title', 'created_at', 'updated_at',     
        ]

    def create(self, validated_data):
        return Question(**validated_data)