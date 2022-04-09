from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from rest_framework import status
from .models import Employee

# Create your views here.
class EmployeeApiView(APIView):
    def post(self, request):
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            item = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Employee.objects.all()
        serializer = EmployeeSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def patch(self, request, id=None):
        item = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


    def delete(self, request, id=None):
        item = get_object_or_404(Employee, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})

    def put(self, request, id=None):
        item = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(item, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})