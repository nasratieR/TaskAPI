from django.contrib.auth.models import User, Group
from rest_framework import serializers
from taskusers.tasks.serializers import TaskSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    #tasks = TaskSerializer(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']