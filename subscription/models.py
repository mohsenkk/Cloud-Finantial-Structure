from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    credit = models.DecimalField(max_digits=10, decimal_places=2)

class Subscription(models.Model):
    name = models.CharField(max_length=255)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Invoic(models.Model):
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)