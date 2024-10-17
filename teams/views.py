from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TeamSerializer
from .models import TeamModel
from .permissions import IsAdminOrReadOnly


# Create your views here.
class TeamViews(APIView):
    permission_classes = [IsAdminOrReadOnly]  # Only admin users can perform CRUD operations on teams.
    def get(self, request):
        teams = TeamModel.objects.filter(name__icontains= "")
        serializer = TeamSerializer(teams, many=True)
        # print(serializer)
        return  Response({'message': 'Teams get request Successful', 'teams': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        data_copy = request.data.copy()
        data_copy['user'] = request.user.id   
        
        serializer = TeamSerializer(data=data_copy)
        if  serializer.is_valid():
            serializer.save()
            return Response({"message": "Team post request was successful"}, status=status.HTTP_200_OK)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def  put(self, request, id):
        try:
            team = TeamModel.objects.get(id=id)
        except TeamModel.DoesNotExist:
            return Response({"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Team update request was successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def  delete(self, request, id):
        try:
            team = TeamModel.objects.get(id=id)
        except TeamModel.DoesNotExist:
            return Response({"message": "Team data does not exist"}, status=status.HTTP_404_NOT_FOUND)
        team.delete()
        return Response({"message": "Team data deleted successful"}, status=status.HTTP_200_OK)