from django.urls import path
from .views import RegisterView, TaskListCreate, TaskDetail

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("tasks/", TaskListCreate.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetail.as_view(), name="task-detail"),
]
