from django.urls import path


from API import views

urlpatterns = [
    path('', views.getRoutes),
    path ('task-list/<str:pk>/', views.getTaskList, name='task-list'),
    path ('task-details/<str:pk>/', views.getTask, name='task-detail'),
    path ('task-create/', views.createTask, name='task-create'),
    path ('task-update/<str:pk>/', views.updateTask, name='task-update'),
    path ('task-delete/<str:pk>/', views.deleteTask, name='task-delete'),
    
    path ("home/",views.home, name ="home"),
    path ("login/",views.LogingPage, name ="login"),
    path ('register/', views.registerUser , name = 'register'),
    path ("logout/", views.logoutUser , name ='logout'),
    

]
