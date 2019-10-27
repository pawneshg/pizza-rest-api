from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user profiles."""

    def create_user(self, email, name, password=None):
        """create a new user profile."""
        if not email:
            raise ValueError("User must have email address.")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """New super user with given details."""
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """reterive full name of the user."""
        return self.name

    def get_short_name(self):
        """Retrieve short name of user."""
        return self.name

    def __str__(self):
       """string representation"""
       return self.email

class PizzaOrderDetails(models.Model):
    """Database model for order in the system."""
    PIZZA_SIZE = (
       ('regular', 'Regular'),
       ('medium', 'Medium'),
       ('large', 'Large')
    )
    order_id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True, null=True)
    #user = models.ForeignKey(User, default=1, on_delete='cascade')
    flavours = models.CharField(max_length=20, blank=False, default='')
    count = models.IntegerField() # add validation Todo
    size = models.CharField(choices=PIZZA_SIZE, default='regular', max_length=20)
    delivery_status = models.CharField(max_length=20)
    tracking_info = models.TextField(blank=True, null=True)
