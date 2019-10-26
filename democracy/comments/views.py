from django.shortcuts import render
from rest_framework.views import APIView
from .models import Comment


class ListComments(APIView):
    """
    View to list all comments in the system.

    * Requires jwt authentication.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        # comments = [user.username for user in User.objects.all()]
        comments = Comment.objects.all()
        return Response(comments)
