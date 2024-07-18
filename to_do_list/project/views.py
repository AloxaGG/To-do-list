from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Task, Group
from .serializers import TaskSerializer, GroupSerializer
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse



class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

class GroupListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class GroupRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class TaskView(View):
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'tasks.html', {'tasks': tasks})

    def post(self, request):
        # Обработка создания новой задачи
        return JsonResponse({'message': 'Новая задача успешно создана'}, status=201)

class GroupView(View):
    def get(self, request):
        groups = Group.objects.all()
        return render(request, 'groups.html', {'groups': groups})

    def post(self, request):
        # Обработка создания новой группы
        return JsonResponse({'message': 'Новая группа успешно создана'}, status=201)