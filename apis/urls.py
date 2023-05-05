from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('subscription', views.SubscriptionViewSet, 'subscription')
router.register('invoice', views.InvoiceViewSet, 'invoice')
router.register('activate/(?P<pk>[^/.]+)', views.ActivationViewSet, 'activate')
router.register('deactivate/(?P<pk>[^/.]+)', views.DeactivationViewSet, 'deactivate')


# URLConf
urlpatterns = [

]

urlpatterns += router.urls

