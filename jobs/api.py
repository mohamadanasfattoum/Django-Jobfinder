from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import BasePermission #, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response




from .serializers import JobListSerializer, JobDetailSerializer
from .models import Job

# class ReadOnly(BasePermission):
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS

class JobListApi(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    serializer_class = JobListSerializer
    queryset = Job.objects.all()

# def get(self, request, format=None):
#         content = {
#             'status': 'request was permitted'
#         }
#         return Response(content)


class JobDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobDetailSerializer
    queryset = Job.objects.all()