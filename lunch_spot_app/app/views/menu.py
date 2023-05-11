from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Menu
from ..serializer import MenuSerializer

@api_view(["POST"])
def update_menu(request, pk):
    menu = Menu.objects.get(pk=pk)
    data = MenuSerializer(menu, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def current_day_menu(request):
    menu = Menu.objects.filter(auto_now=True)
    if menu:
        serializer = MenuSerializer(menu, many=True)
        return Response(serializer.data)
    else:
        return Response("No menu found", status=status.HTTP_404_NOT_FOUND)