from django.db import models

# todo item
class Task(models.Model):
    text = models.CharField(max_length=64)                  # eg: Homework #1
    class_name = models.CharField(max_length=16)             # eg: CENG112
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    isDone = models.BooleanField(default=False)