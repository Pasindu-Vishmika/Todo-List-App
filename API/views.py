from django.http import  JsonResponse , HttpResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializer import TaskSerializer

# Create your views here.


@api_view(['GET'])
def getRoutes (request):
    routes = {
            'List': '/task-list/',
            'Detail View': '/task-detail/<str:pk>/',
            'Create': '/task-create/',
            'Update': '/task-update/<str:pk>/',
            'Delete': '/task-delete/<str:pk>/',
        }
    return Response( routes)

@api_view(['GET'])
def getTaskList (request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response (serializer.data)

@api_view(['GET'])
def getTask (request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks , many=False)
    return Response (serializer.data)

def createTask (request):
    return Response ('create')
