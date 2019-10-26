from django.db import models
import uuid

# Create your models here.
class Comment(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent_uuid = models.CharField(max_length=100, default='0000000',)
    user_uuid = models.CharField(max_length=100)
    target_uuid = models.CharField(max_length=100)  # Target is the UUID of the thing that this comment applies to 
    content = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
