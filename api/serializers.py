from statistics import mode
from rest_framework import serializers
from . import models

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        exclude = ["active"]