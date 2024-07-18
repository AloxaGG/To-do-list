from django.urls import path
from .views import *

urlpatterns = [
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),
    path('api/groups/', GroupListCreateView.as_view(), name='group-list-create'),
    path('api/groups/<int:pk>/', GroupRetrieveUpdateDestroyView.as_view(), name='group-retrieve-update-destroy'),
    path('tasks/', TaskView.as_view(), name='tasks-view'),
    path('groups/', GroupView.as_view(), name='groups-view'),
]