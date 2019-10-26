from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Question, Choice
from .serializers import QuestionSerializer, PollSerializer, ChoiceSerializer

class PollsViewSet(viewsets.ModelViewSet) :
    """A poll is a question and all possible choices. 
    """
    serializer_class = PollSerializer
    queryset = Question.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Question.objects.all()
        serializer = PollSerializer(Question.objects.all(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Question.objects.all()
        queryset = queryset.filter(uuid=pk)
        if not queryset:
            queryset = Question.objects.none()
        
        serializer = PollSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        raise NotImplementedError("YOU CANNOT MAKE QUESTIONS YET!!! >:-| ")
        # serializer = CommentSerializer(data=request.data)
        # if serializer.is_valid():
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionViewSet(viewsets.ModelViewSet) :
    """A viewset for getting a list of all polls, but just their titles, not 
    the results/choices. 
    """
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Question.objects.all()
        serializer = QuestionSerializer(Question.objects.all(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Question.objects.all()
        queryset = queryset.filter(target_uuid=pk)
        if not queryset:
            queryset = Question.objects.none()

        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = serializer.save()
            question.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChoiceViewSet(viewsets.ModelViewSet) :
    """A viewset for getting the choices associated with a question. 
    """
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()

    def retrieve(self, request, pk=None):
        queryset = Choice.objects.all()
        queryset = queryset.filter(target_uuid=pk)
        if not queryset:
            queryset = Choice.objects.none()

        serializer = ChoiceSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            choice = serializer.save()
            choice.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)