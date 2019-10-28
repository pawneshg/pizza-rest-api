from django.db import models
from django.db.models import QuerySet


class OrderQuerySet(QuerySet):
    """Order Query Set."""
    # def get_customers_order(self, name):
    #     return self.filter(customer=name)
    #
    # def get_orders_by_status(self, status):
    #     return self.filter(status=status)
    #
    # def update_an_order(self, id_, data):
    #     return self.filter(order_id=id_).update(**data)

    def create_order(self, data):
        return self.create(**data)

class OrderManager(models.Manager):
    """Interface for the PizzaOrderDetails."""
    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)

    # def get_customers_order(self, name):
    #     return self.get_queryset().get_customers_order(name)
    #
    # def get_orders_by_status(self, status):
    #     return self.get_queryset().get_orders_by_status(status)
    #
    # def update_an_order(self, id_, data):
    #     return self.get_queryset().update_an_order(id_, data)

    def create_order(self, data):
        return self.get_queryset().create_order(data)
