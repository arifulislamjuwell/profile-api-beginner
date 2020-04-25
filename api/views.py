from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):

    def get(self, request, format= None):

        api_view=[
            'api testing',
            'i think it should be work'
        ]
        return Response({'message': 'api_test', 'api_test':api_view})