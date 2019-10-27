from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pizza_api import views
#from django.conf.urls import url
# from rest_framework_swagger.views import get_swagger_view
#
# schema_view = get_swagger_view(title='PizzaOrder API')
#
# urlpatterns = [
#     url(r'^$', schema_view)
# ]

router = DefaultRouter()
router.register('pizza-viewset', views.PizzaViewSet, base_name='pizza-viewset')
#router.register('pizza', views.PizzaViewSet)
urlpatterns = [
    # path('', include(router.urls)),
    # path('docs/', include('rest_framework_swagger.urls')),
    #url(r'^docs/', include('rest_framework_swagger.urls')),
]
urlpatterns += router.urls
