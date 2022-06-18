from django.urls import path
from . import views

urlpatterns = [
    path('create-todo/', views.createTodo, name="create-task"),
    path('list-todo/', views.todoList, name="list-todo"),
    path('get-todoDetail/<str:pk>/', views.todoDetail, name="todo- details"),
    path('update-todo/<str:pk>/', views.todoUpdate, name="update-task"),
    path('delete-todo/<str:pk>/', views.todoDelete, name="delete-task")
]
