from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pizza_api import views


router = DefaultRouter()
router.register('pizza-viewset', views.PizzaViewSet, base_name='pizza-viewset')

urlpatterns = [
    path('', include(router.urls)),
]
