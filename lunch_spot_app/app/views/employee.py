from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Employee
from ..serializer import EmployeeSerializer


@api_view(["POST"])
def add_employee(request):
    employee = EmployeeSerializer(data=request.data)

    if Employee.objects.filter(**request.data).exists():
        raise serializers.ValidationError("Item already exists")
    if employee.is_valid():
        employee.save()
        return Response(employee.data)
    else:
        return Response(employee.errors, status=status.HTTP_400_BAD_REQUEST)
