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
        print('-----------',request.user.customer.id,'--------------')
        subscriptions = Subscription.objects.filter(customer__id=request.user.customer.id).select_related('customer').all()
        serializer = SubscriptionSerializer(
            subscriptions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print(request.data)
        serializer = SubscriptionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(customer=request.user.customer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


