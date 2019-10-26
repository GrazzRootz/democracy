from django.db import models

# Create your models here.
class Comment(models.Model):
    uuid = models.CharField(max_length=100)
    # Target is the UUID of the thing that this comment applies to 
    target_uuid = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
