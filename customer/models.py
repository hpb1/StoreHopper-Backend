from django.db import models
import uuid
from django.contrib.auth import get_user_model
from owner.models import Store
# Create your models here.

User = get_user_model()

class ItemRequest(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    items = models.TextField()
    message = models.TextField()