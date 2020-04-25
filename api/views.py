from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer

class HelloApiView(APIView):

    serializer_class= HelloSerializer

    def get(self, request, format= None):

        api_view=[
            'api testing',
            'i think it should be work'
        ]
        return Response({'message': 'api_test', 'api_test':api_view})

    def post(self, request):

        serializer= self.serializer_class(data= request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message= 'hello {}'.format(name)
            return Response ({'message': message})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self,request, pk=None):
        return Response({'response': 'PUT'})
    
    def patch(self, request, pk=None):
        return Response({'response': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'response': 'DELETE'})