from datetime import timedelta
from celery import shared_task
from subscription.models import Subscription, Invoice, Customer
from django.utils import timezone


def create_one_invoice(subscription, customer):
    Invoice.objects.create(subscription=subscription)
    customer.credit -= subscription.unit_price
    customer.save()


@shared_task
def invoice_creator():

    subscriptions = Subscription.objects.filter(is_active=True)
    for subscription in subscriptions:
        customer = Customer.objects.get(subscriptions__id=subscription.id)
        last_invoice = Invoice.objects.filter(subscription__id=subscription.id).order_by('-start_date').first()

        if last_invoice is not None:
            print(last_invoice.id, (timezone.now() - last_invoice.start_date) >= timedelta(seconds=30))
            if (timezone.now() - last_invoice.start_date) >= timedelta(seconds=30):
                last_invoice.end_date = timezone.now()
                last_invoice.save()
                if customer.credit < subscription.unit_price:
                    subscription.is_active = False
                    subscription.save()
                else:
                    create_one_invoice(subscription, customer)
        else:
            create_one_invoice(subscription, customer)

