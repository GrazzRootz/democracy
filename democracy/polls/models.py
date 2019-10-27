from django.db import models
import uuid

# Create your models here.
class Question(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # What user has created the poll and what 
    user_uuid = models.CharField(max_length=100)
    # What other item (garden/event) this is associated with
    target_uuid = models.CharField(max_length=100, default=None)
    
    # The actual question of the Poll 
    title = models.TextField(max_length=100)
    
    # Timing information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Choice(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.TextField(max_length=200)
    votes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
