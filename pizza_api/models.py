from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class ObjectTracking(models.Model):
    """Basic database model."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)

class OrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()

    def all_objects(self):
        return super().get_queryset()


class PizzaOrderDetails(ObjectTracking):
    """Database model for order in the system."""
    PIZZA_SIZE = (
       ('regular', 'Regular'),
       ('medium', 'Medium'),
       ('large', 'Large')
    )
    order_id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True, null=True)
    flavours = models.CharField(max_length=20, blank=False, default='')
    count = models.PositiveIntegerField() # add validation Todo
    size = models.CharField(choices=PIZZA_SIZE, default='regular', max_length=20)
    delivery_status = models.CharField(max_length=20, default='pending')
    tracking_url = models.URLField(max_length=250)
    customer_name = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    customer_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)

    objects = OrderManager()

    def __str__(self):
        return self.description
