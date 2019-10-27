from rest_framework import serializers
from pizza_api.models import PizzaOrderDetails


class PizzaOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaOrderDetails
        fields = [
            "order_id",
            "description",
            "created_by",
            "price",
            "flavours",
            "count",
            "size",
            "customer_name",
            "customer_phone_number"

        ]
        read_only_fields = ["order_id"]

    def create(self, validated_data):
        """Create the Order."""
        validated_data.update({'tracking_url': 'https://trackmyorder.com'})
        order = PizzaOrderDetails.objects.create(**validated_data)
        return order

    def update(self, instance, validated_data):
        """Update the Order details."""
        instance = super().update(instance, validated_data)

        return instance
