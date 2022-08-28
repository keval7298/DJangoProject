from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(self, request, format=None):
        return Response({'message':'This response is from ApiView', 'status':200})
