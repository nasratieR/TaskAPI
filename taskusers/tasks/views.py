from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import TasksModel
from rest_framework import permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404


class TasksViewSet(viewsets.ModelViewSet):
    queryset = TasksModel.objects.all()
    
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    @swagger_auto_schema(
        operation_description="Create task",
        responses={201: openapi.Response('Task created', TaskSerializer)},
        response_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'exampleTest': openapi.Schema(type=openapi.TYPE_STRING, description='Example description'),

            },
            required=['exampleTest']
        )
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
    operation_description="Retrieve a task",
    responses={200: TaskSerializer},
    )
    def retrieve(self, request, *args, **kwargs):
        task_id = kwargs.get('pk')
        task = get_object_or_404(TasksModel, pk=task_id)

        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Update task",
        responses={200: openapi.Response('Task updated', TaskSerializer)}
    )
    def partial_update(self, request, *args, **kwargs):
        task_id = kwargs['pk']
        task = get_object_or_404(TasksModel, pk=task_id)

        serializer = self.get_serializer(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
    operation_description="Destroy task",
    responses={204: "Task successfully deleted"}
    )
    def destroy(self, request, *args, **kwargs):
        task_id = kwargs['pk']
        task = get_object_or_404(TasksModel, pk=task_id)

        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
