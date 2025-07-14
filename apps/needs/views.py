from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import NeedsListSerializer,AddNeedsSerializer, NeedsDetailsSerializer, UpdateNeedsSerializer
from .models import Needs
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class NeedsListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = Needs.objects.all()
        serializer = NeedsListSerializer(queryset, many=True)
        return Response({
            "message": "Needs retrieved successfully.",
            "status_code": 200,
            "data": serializer.data
        })

class AddNeedsAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        # Logic to handle POST request for creating a new need
        serializer = AddNeedsSerializer(data=request.data)
        if serializer.is_valid():
            # Automatically set the user to the current authenticated user
            serializer.save(user=request.user)
            return Response({
                "message": "Need created successfully.",
                "status_code": "201",
                "data": serializer.data
            })
        return Response({
            "message": "Failed to create need.",
            "status_code": "400",
            "data": serializer.errors
        })
        

class NeedsDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        try:
            need = Needs.objects.get(id=pk)
            serializer = NeedsDetailsSerializer(need)
            return Response({
                "message": "Need details retrieved successfully.",
                "status_code": "200",
                "data": serializer.data
            })
        except Needs.DoesNotExist:
            return Response({
                "message": "Need not found.",
                "status_code": "404"
            }, status=404)


class NeedsUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, pk):
        try:
            need = Needs.objects.get(id=pk)
        except Needs.DoesNotExist:
            return Response({
                "message": "Need not found.",
                "status_code": "404"
            }, status=404)

        # Check if the current user is the owner of the need
        if need.user != request.user:
            return Response({
                "message": "You don't have permission to update this need.",
                "status_code": "403"
            }, status=403)

        serializer = UpdateNeedsSerializer(need, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Need updated successfully.",
                "status_code": "200",
                "data": serializer.data
            })
        return Response({
            "message": "Failed to update need.",
            "status_code": "400",
            "data": serializer.errors
        })                                                                                                                    

class NeedsDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            need = Needs.objects.get(id=pk)
        except Needs.DoesNotExist:
            return Response({
                "message": "Need not found.",
                "status_code": "404"
            }, status=404)

        # Check if the current user is the owner of the need
        if need.user != request.user:
            return Response({
                "message": "You don't have permission to delete this need.",
                "status_code": "403"
            }, status=403)

        need.delete()
        return Response({
            "message": "Need deleted successfully.",
            "status_code": "204",
        })  

