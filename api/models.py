from django.db import models

# todo item
class Task(models.Model):
    text = models.CharField(max_length=64)                  # eg: Homework #1
    class_name = models.CharField(max_length=16)             # eg: CENG112
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.class_name + " - " + self.text