from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('subscription', views.SubscriptionViewSet, 'subscription')
router.register('activate/(?P<pk>[^/.]+)', views.ActivationViewSet, 'activate')


# URLConf
urlpatterns = [

]

urlpatterns += router.urls

