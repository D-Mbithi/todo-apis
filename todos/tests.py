from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Todo


# Create your tests here.
class TodoModelTestCase(TestCase):
    """Todo model test."""

    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(title="first todo", task="first task todo")

    def test_model_content(self):
        self.assertEqual(self.todo.title, "first todo")
        self.assertEqual(self.todo.task, "first task todo")
        self.assertEqual(str(self.todo), "first todo")

    def test_api_listview(self):
        response = self.client.get(reverse("todos:todo_list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        response = self.client.get(
            reverse("todos:todo_detail", kwargs={"pk": self.todo.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "first todo")
