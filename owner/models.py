from django.db import models
from django.contrib.auth import get_user_model
import uuid
# Create your models here.

User = get_user_model()

class Store(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField(default=None)
    items_list = models.TextField(default=None)
    address = models.TextField()
    city = models.TextField()
    peak_time = models.CharField(max_length=30, default=None)
    pin_code = models.CharField(max_length=10)
    latitude = models.CharField(max_length=30)
    longitude = models.CharField(max_length=30)
