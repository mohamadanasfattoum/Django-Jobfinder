from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import BasePermission 


from .serializers import JobListSerializer, JobDetailSerializer
from .models import Job

class JobListApi(generics.ListCreateAPIView):
    serializer_class = JobListSerializer
    queryset = Job.objects.all()



class JobDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobDetailSerializer
    queryset = Job.objects.all()