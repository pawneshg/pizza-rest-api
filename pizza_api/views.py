from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from pizza_api import serializers
from .models import PizzaOrderDetails

# class PizzaApiView(APIView):
#     """Pizza API View"""
#     serializer_class = serializers.HelloSerializer
#
#     def get(self, request, format=None):
#         """Returns a list of APIView features"""
#         an_apiview = [
#             'uses HHTTP methods as function (get, post, patch, put, delete)',
#             'Is similar to a traditional Django View',
#             'Gives you the most control over you app logic',
#             'is mapped manually to URLS.'
#         ]
#         return Response({'message': 'Hello', 'an_apiview': an_apiview})
#
#     def post(self, request):
#         """create"""
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             message = f"Hello {name}"
#             return Response({'message': message})
#         else:
#             return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST)
class PizzaViewSet(viewsets.ViewSet):
    """Pizza View set apis."""
# class PizzaViewSet(viewsets.ModelViewSet):
#     """Pizza View set apis."""
    # serializer_class = serializers.PizzaOrderSerializer
    # queryset = models.PizzaOrderDetails.objects.all()
    serializer_class = serializers.PizzaOrderSerializer

    def list(self, request):
        """list out all the orders."""
        orders = PizzaOrderDetails.objects.all()
        serializer = self.serializer_class(orders, many=True)
        return Response({'message': 'Successfully Retrieved.', 'orders': serializer.data})

    def retrieve(self, request, pk=None):
        """retrieve the order details based on id."""
        try:
            order = PizzaOrderDetails.objects.get(pk=pk)
        except PizzaOrderDetails.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(order)
        return Response({'message': 'Successfully Retrieved.', 'order': serializer.data})

    def destroy(self, request, pk=None):
        """Delete an order details."""
        PizzaOrderDetails.objects.filter(pk=pk).delete()
        return Response({'message': 'Successfully Deleted the order details.'})

    def update(self, request, pk=None):
        """update the order details."""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            PizzaOrderDetails.objects.filter(order_id=pk).update(**serializer.validated_data)
        return Response({'message': 'Updated the Order details.', 'updated_data': []})

    def create(self, request):
        """Create an order for the pizza. """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            PizzaOrderDetails.objects.create(**serializer.validated_data)
            return Response({'message': 'created.', 'status':status.HTTP_201_CREATED})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
