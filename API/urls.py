from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from API import views

urlpatterns = [
    path('', views.getRoutes),
    path ('task-list/', views.getTaskList, name='task-list'),
    path ('task-details/<str:pk>/', views.getTask, name='task-detail'),
    path ('task-create/', views.createTask, name='task-create'),
    path ('task-update/<str:pk>/', views.updateTask, name='task-update'),
    path ('task-delete/<str:pk>/', views.deleteTask, name='task-delete'),

]
