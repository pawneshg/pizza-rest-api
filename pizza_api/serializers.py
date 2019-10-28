from rest_framework import serializers
from pizza_api.models import PizzaOrderDetails
from pizza_project import utils

SERLIZER_LOGGER = utils.create_logger_module('pizza_serilizer')

class PizzaOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaOrderDetails
        # fields = '__all__'
        fields = [
            "order_id",
            "description",
            "created_by",
            "price",
            "flavours",
            "count",
            "size",
            "customer",
            "customer_phone_number",
            "status",
            "tracking_url"

        ]
        read_only_fields = ["order_id"]

    def create(self, validated_data):
        """Create the Order."""
        validated_data.update({'tracking_url': 'https://trackmyorder.com'})
        order = PizzaOrderDetails.objects.create_order(validated_data)
        return order

    def update(self, instance, validated_data):
        """Update the Order details."""
        # request = self.context.get('request')
        try:
            SERLIZER_LOGGER.info("Updating.. instance= %s ,data= %s", instance, validated_data)
            if instance.status not in ['delivered']:
                instance.description = validated_data.get("description", instance.description)
                instance.created_by = validated_data.get("created_by", instance.created_by)
                instance.price = validated_data.get("price", instance.price)
                instance.flavours = validated_data.get("flavours", instance.flavours)
                instance.count = validated_data.get("count", instance.count)
                instance.status = validated_data.get("status", instance.status)
                instance.size = validated_data.get("size", instance.size)
                instance.save()

        except BaseException as error:
            SERLIZER_LOGGER.error(error)
        return instance


