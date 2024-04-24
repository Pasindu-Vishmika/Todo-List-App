from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from .models import Task 
from .serializer import TaskSerializer
from django.contrib.auth.models import User



@api_view(['GET'])
def getRoutes(request):
    routes = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(routes)

@api_view(['GET'])
def getTaskList(request):
    tasks = Task.objects.all().order_by('-created')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTask (request,pk):
    try:
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task , many=False)
        return Response (serializer.data)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def createTask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view([ 'PUT', 'PATCH'])
def updateTask(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    elif request.method in ('PUT', 'PATCH'):
        partial = request.method == 'PATCH'  # True for PATCH requests
        serializer = TaskSerializer(task, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteTask (request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.delete()
        return Response('Task deleted successfully')
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)