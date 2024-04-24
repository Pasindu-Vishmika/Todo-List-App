from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from API import views

urlpatterns = [
    path('', views.getRoutes ),
    path ('task-list/', views.getTaskList, name='task-list'),
    path ('task-details/<str:pk>/', views.getTask, name='task-detail'),
    path ('task-create/', views.createTask, name='task-create'),
    path ('task-update/<str:pk>/', views.updateTask, name='task-update'),
    path ('task-delete/<str:pk>/', views.deleteTask, name='task-delete'),
    
    path ("token/" , obtain_auth_token , name= 'token'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

]
