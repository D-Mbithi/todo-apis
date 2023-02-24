from django.urls import path

from .views import DetailTodoApiView, ListTodoApiView

app_name = "todos"

urlpatterns = [
    path("<int:pk>", DetailTodoApiView.as_view(), name="todo_detail"),
    path("", ListTodoApiView.as_view(), name="todo_list"),
]
