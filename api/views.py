from django.shortcuts import render
from django.http import JsonResponse
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import generics, viewsets
# Create your views here.
# viewsets.ModelViewSet

def todos(request):
	return JsonResponse({'name':'Hello There'})

class TodoViewSet(viewsets.ModelViewSet):
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer

# class TodoLol(generics.RetrieveUpdateDestroyAPIView):
# 	queryset = Todo.objects.all()
# 	serializer_class = TodoSerializer