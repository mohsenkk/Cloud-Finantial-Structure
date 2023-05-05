from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('subscription/v2', views.SubscriptionViewSet, 'subscription')

# URLConf
urlpatterns = [
    path('subscription/', views.subscription_view),
]

urlpatterns += router.urls

