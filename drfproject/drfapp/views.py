from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class Testview(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username' : 'admin', 
            'years-active' : 20
        }

        return Response(data)
