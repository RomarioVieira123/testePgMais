from rest_framework import serializers

from telephone_operator.serializers import TelephoneOperatorSerializerBroker
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    operator = TelephoneOperatorSerializerBroker(read_only=True)

    class Meta:
        model = Message
        fields = ['idmensagem', 'operator']

