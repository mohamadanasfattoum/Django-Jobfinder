from rest_framework import serializers
from .models import Job

class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields='__all__'



