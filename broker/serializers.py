from rest_framework import serializers
from .models import Broker


class BrokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broker
        fields = ['id']
