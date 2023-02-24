from rest_framework import generics

from .models import Todo
from .serializers import TodoSerializer


class ListTodoApiView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodoApiView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
