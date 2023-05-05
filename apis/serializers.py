from decimal import Decimal
from subscription.models import Subscription
from rest_framework import serializers


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'name', 'unit_price', 'is_active', 'customer']
        extra_kwargs = {'customer': {'required': False}} 

