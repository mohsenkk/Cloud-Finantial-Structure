from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from django.db.models import Sum

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

class InvoicehistoryViewSet(GenericViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = SubscriptionSerializer

    def list(self, request):
        customer = self.request.user.customer
        cost = Invoice.objects.filter(subscription__customer=customer).aggregate(Sum('subscription__unit_price'))['subscription__unit_price__sum']
        number_of_invoices = Invoice.objects.filter(subscription__customer=customer).count()
        serializer = InvoiceSerializer(Invoice.objects.filter(subscription__customer=customer), many=True)
        return Response({"cost": cost ,"number of invoices": number_of_invoices,"invoices": serializer.data})
