from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DriverSerializer
from .models import DriverModel
from teams.permissions import IsAdminOrReadOnly


# Create your views here.
class DriverViews(APIView):
    permission_classes = [IsAdminOrReadOnly]  # Only admin users can perform CRUD operations on teams.
    def get(self, request):
        drivers = DriverModel.objects.filter(name__icontains= "")
        serializer = DriverSerializer(drivers, many=True)
        # print(serializer)
        return  Response({'message': 'Drivers get request Successful', 'teams': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        data_copy = request.data.copy()
        data_copy['user'] = request.user.id   
        
        serializer = DriverSerializer(data=data_copy)
        if  serializer.is_valid():
            serializer.save()
            return Response({"message": "Driver post request was successful"}, status=status.HTTP_200_OK)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def  put(self, request, id):
        try:
            team = DriverModel.objects.get(id=id)
        except DriverModel.DoesNotExist:
            return Response({"message": "Driver not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = DriverSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Driver update request was successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def  delete(self, request, id):
        try:
            team = DriverModel.objects.get(id=id)
        except DriverModel.DoesNotExist:
            return Response({"message": "Driver data does not exist"}, status=status.HTTP_404_NOT_FOUND)
        team.delete()
        return Response({"message": "Driver data deleted successful"}, status=status.HTTP_200_OK)