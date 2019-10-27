from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from pizza_api import serializers
from .models import PizzaOrderDetails


class PizzaViewSet(viewsets.ModelViewSet):
    """Pizza View set apis."""
    serializer_class = serializers.PizzaOrderSerializer
    queryset = PizzaOrderDetails.objects.all()
    lookup_field = 'order_id'
