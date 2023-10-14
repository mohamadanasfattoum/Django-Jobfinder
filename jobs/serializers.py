from rest_framework import serializers
from .models import Job

class JobListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields='__all__'


class JobDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields='__all__'

'''

class JobUpateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Job
        fields='__all__'
'''
