from django.db import models

from shareds.models import Stat
from telephone_operator.models import TelephoneOperator


class Message(models.Model):
    idmensagem = models.CharField(max_length=50, default=False)
    operator = models.ForeignKey(TelephoneOperator, related_name='message', on_delete=models.CASCADE)
    stat = models.OneToOneField(Stat, related_name='message', on_delete=models.CASCADE)
    message = models.CharField(max_length=140, default='')
    destination_number = models.CharField(max_length=9, default=False)
    shipping_time = models.CharField(max_length=8, default='')
    created_at = models.DateTimeField(auto_now_add=True)
