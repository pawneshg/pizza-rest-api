from rest_framework import serializers
from pizza_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a input fields for testing our APIView"""
    name = serializers.CharField(max_length=10)

# class PizzaOrderSerializer(serializers.ModelSerializer):
#     """Serializes a order object."""
#     class Meta:
#         model = models.PizzaOrderDetails
#         fields = ('id', 'flavours', 'count')
#         extra_kwargs = {
#            'tracking_info':{
#                 'write_only': True
#            }
#         }

class PizzaOrderSerializer(serializers.Serializer):
    """Serializes a order object."""
    order_id = serializers.IntegerField()
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    #user = models.ForeignKey(User, default=1, on_delete='cascade')
    flavours = serializers.CharField(max_length=20, default='')
    count = serializers.IntegerField() # add validation Todo
    size = serializers.ChoiceField(choices=['regular', 'medium', 'large'], style={'base_template': 'radio.html'})
    delivery_status = serializers.ChoiceField(choices=['dispatched', 'inprogress', 'delivered'], style={'base_template': 'radio.html'})
    #tracking_info = serializers.CharField(style={'base_template': 'textarea.html'})
