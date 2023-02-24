from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    task = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'
        ordering = ['-created']

    def __str__(self):
        return self.title
