from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Comment
from .serializers import CommentSerializer 

class CommentsViewSet(viewsets.ModelViewSet) :
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Comment.objects.all()
        serializer = CommentSerializer(Comment.objects.all(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Comment.objects.all()
        queryset = queryset.filter(target_uuid=pk)
        if not queryset:
            queryset = Comment.objects.none()
        
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)