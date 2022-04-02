from rest_framework.views import APIView
from rest_framework.response import Response

class TestView(APIView):
    def get(self, request):
        key = "visitCount"
        if key in request.session: request.session[key] += 1
        else: request.session[key] = 1

        content = {"msg":"hello", key:request.session[key]}
        return Response(content)
