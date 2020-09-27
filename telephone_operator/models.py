from django.db import models
from broker.models import Broker


class TelephoneOperator(models.Model):
    broker = models.ForeignKey(Broker, related_name='broker', on_delete=models.CASCADE)
    operator = models.CharField(max_length=50, default='')
    created_at = models.DateTimeField(auto_now_add=True)
