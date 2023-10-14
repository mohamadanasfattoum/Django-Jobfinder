from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JobListSerializer
from .models import Job


class JobListApi(generics.ListAPIView):
    serializer_class = JobListSerializer
    queryset = Job.objects.all()