from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

class TestView(APIView):
    def get(self, request):
        key = "visitCount"
        if key in request.session: request.session[key] += 1
        else: request.session[key] = 1

        content = {"msg":"hello", key:request.session[key]}
        return Response(content)


class TaskView(APIView):
    def get(self, request):
        queryset = Task.objects.filter(active=True)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)