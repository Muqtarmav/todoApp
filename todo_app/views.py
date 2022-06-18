from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import  Response

from . import serializer
from .models import Todo
from . serializer import TodoSerializer

@api_view(['POST'])
def createTodo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def todoList(request):
    todo = Todo.objects.all()
    serializer = TodoSerializer(todo, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def todoDetail(request, pk):
    todo = Todo.objects.get(id=pk)
    serializers = TodoSerializer(todo, many=False)
    return Response(serializers.data)

@api_view(['POST'])
def todoUpdate(request, pk):
    todo = Todo.objects.get(id=pk)
    serializers = TodoSerializer(instance= todo, data=request.data)

    if serializers.is_valid():
        serializers.save()

    return Response(serializers.data)

@api_view(['DELETE'])
def todoDelete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()

    return Response(serializer.data)
