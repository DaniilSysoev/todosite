from django.urls import path
from todolist.views import TaskListAPIView, TaskDetailAPIView


urlpatterns = [
    path('todo/', TaskListAPIView.as_view()),
    path('todo/<int:pk>/', TaskDetailAPIView.as_view())
]
