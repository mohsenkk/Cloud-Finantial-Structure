from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('subscription/', views.subscription_view),
]
