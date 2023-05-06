from decimal import Decimal
from subscription.models import Subscription, Invoice
from rest_framework import serializers


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'name', 'unit_price', 'is_active', 'customer']
        extra_kwargs = {'customer': {'required': False}} 

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'start_date', 'end_date', 'subscription']
        extra_kwargs = {'subscription': {'required': False}} 

