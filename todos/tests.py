from django.test import TestCase

from .models import Todo


# Create your tests here.
class TodoModelTestCase(TestCase):
    """Todo model test."""

    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title='first todo',
            task='first task todo'
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, 'first todo')
        self.assertEqual(self.todo.task, 'first task todo')
        self.assertEqual(str(self.todo), 'first todo')
