from datetime import timedelta
from celery import shared_task
from subscription.models import Subscription, Invoice, Customer
from django.utils import timezone


@shared_task
def invoice_creator():

    subscriptions = Subscription.objects.filter(is_active=True)
    for subscription in subscriptions:
        last_invoice = Invoice.objects.filter(subscription__id=subscription.id).order_by('-start_date').first()

        if last_invoice is not None:
            if timezone.now() - last_invoice.start_date >= timedelta(seconds=30):
                last_invoice.end_date = timezone.now()
                if Customer.objects.get(subscriptions__id=subscription.id).credit < subscription.unit_price:
                    subscription.is_active = False
                else:
                    Invoice.objects.create(subscription=subscription)
                    Customer.objects.get(subscriptions__id=subscription.id).credit -= subscription.unit_price

        else:
            Invoice.objects.create(subscription=subscription)
            Customer.objects.get(subscriptions__id=subscription.id).credit -= subscription.unit_price
