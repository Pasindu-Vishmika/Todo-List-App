from django.contrib import admin
from django.urls import path

from API import views

urlpatterns = [
    path('', views.getRoutes ),
    path ('task-list/', views.getTaskList, name='task-list'),
    path ('task-details/<str:pk>/', views.getTask, name='task-detail'),
]
