from rest_framework import serializers

from broker.serializers import BrokerSerializer
from .models import TelephoneOperator


class TelephoneOperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelephoneOperator
        fields = ['id', 'operator', 'broker']


class TelephoneOperatorSerializerBroker(serializers.ModelSerializer):
    class Meta:
        model = TelephoneOperator
        fields = ['broker']
