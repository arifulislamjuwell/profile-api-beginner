from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelloSerializer, ProfileSerializer
from .models import UserProfile
from .permissions import ProfilePermission
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request, pk=None):
        return Response({'response': 'PUT'})
    
    def patch(self, request, pk=None):
        return Response({'response': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'response': 'DELETE'})

    
class HelloViewSets(ViewSet):
    serializer_class= HelloSerializer
    def list(self, request):
        api_view=[
            'api testing',
            'i think it should be work'
        ]
        return Response({'message': 'api_test', 'api_test':api_view})

    def create(self,request):
        serializer= self.serializer_class(data= request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message= f'Hellow {name}'
            return Response ({'message': message})
        else:
            return Response(
                serializer.error,
                status= status.HTTP_400_BAD_REQUEST
            )
    
    def retrieve(self, request, pk):
        return Response({'http': 'GET'})

    def update(self, request, pk):
        return Response({'http': 'PUT'})

    def partial_update(self, request, pk):
        return Response({'http': 'PATCH'})

    def destroy(self, request, pk):
        return Response({'http': 'DELETE'})


class ProfileViewSet(ModelViewSet):
    serializer_class= ProfileSerializer
    queryset= UserProfile.objects.all()
    authentication_classes= (TokenAuthentication,)
    permission_classes= (ProfilePermission,)
    filter_backends= (filters.SearchFilter,)
    search_fields= ('name','email',)

class UserLoginApiView(ObtainAuthToken):
    renderer_classes= api_settings.DEFAULT_RENDERER_CLASSES