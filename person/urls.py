#! -*- coding: utf-8 -*-
from django.urls import path, include
from rest_framework import routers

from person import views

router = routers.DefaultRouter()
router.register(r'persons', views.PersonViewSet)
router.register(r'addresses', views.AddressViewSet)


urlpatterns = [
    path('', include(router.urls))
]
