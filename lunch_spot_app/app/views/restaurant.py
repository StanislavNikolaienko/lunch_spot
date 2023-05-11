from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Restaurant
from ..serializer import RestaurantSerializer


@api_view(["POST"])
def add_restaurant(request):
    restaurant = RestaurantSerializer(data=request.data)

    if Restaurant.objects.filter(**request.data).exists():
        raise serializers.ValidationError("Item already exists")
    if restaurant.is_valid():
        restaurant.save()
        return Response(restaurant.data)
    else:
        return Response(restaurant.errors, status=status.HTTP_400_BAD_REQUEST)