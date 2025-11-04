import uuid
from django.db import models

class UserSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

class UploadedImage(models.Model):
    user = models.ForeignKey(UserSession, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    is_garbage = models.BooleanField(null=True)  # True if garbage, False if not
    created_at = models.DateTimeField(auto_now_add=True)
