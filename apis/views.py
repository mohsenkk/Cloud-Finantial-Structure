from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from subscription.models import Subscription, Invoice
from .serializers import SubscriptionSerializer, InvoiceSerializer


class SubscriptionViewSet(mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          GenericViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        customer = self.request.user.customer
        return Subscription.objects.filter(customer=customer)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)



class InvoiceViewSet(mixins.ListModelMixin,
                          GenericViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        customer = self.request.user.customer
        return Invoice.objects.filter(subscription__customer=customer)

    def perform_create(self, serializer):
        serializer.save(subscription__customer=self.request.user.customer)


class ActivationViewSet(GenericViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = SubscriptionSerializer

    def create(self, request, *args, **kwargs):
        Subscription.objects.filter(pk=self.kwargs['pk']).update(is_active=True)
        return Response("Subscription activated successfully.")


class DeactivationViewSet(GenericViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = SubscriptionSerializer

    def create(self, request, *args, **kwargs):
        Subscription.objects.filter(pk=self.kwargs['pk']).update(is_active=False)
        return Response("Subscription deactivated successfully.")

