from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Broker(models.Model):
    name = models.CharField(max_length=75, default='')
    created_at = models.DateTimeField(auto_now_add=True)
