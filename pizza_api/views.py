
from rest_framework import viewsets
from django_filters import rest_framework as filters
from pizza_api import serializers
from .models import PizzaOrderDetails

class PizzaFilter(filters.FilterSet):
    customer = filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = PizzaOrderDetails
        fields = ('status', 'customer')


class PizzaViewSet(viewsets.ModelViewSet):
    """Pizza View set apis."""

    serializer_class = serializers.PizzaOrderSerializer
    queryset = PizzaOrderDetails.objects.all()
    lookup_field = 'order_id'
    filterset_class = PizzaFilter

