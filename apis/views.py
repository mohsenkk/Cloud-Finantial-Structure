from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators  import api_view, authentication_classes, permission_classes
from subscription.models import Customer, Subscription, Invoic
from .serializers import SubscriptionSerializer

@api_view(['GET', 'POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def subscription_view(request, format=None):
    if request.method == 'GET':
        subscriptions = Customer.objects.filter(pk=request.user.id).select_related('subscriptions').all()
        serializer = SubscriptionSerializer(
            subscriptions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SubscriptionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


