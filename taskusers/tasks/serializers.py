from rest_framework import serializers
from .models import TasksModel


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TasksModel
        fields = '__all__'
        
