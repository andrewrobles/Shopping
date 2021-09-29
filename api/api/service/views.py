from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.service.serializers import UserSerializer, GroupSerializer

from api.service.formatting import encode, decode

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!!'})

@api_view(['POST', 'GET'])
def encoder(request):
    if request.method == 'POST':
        return Response({'encoded': encode(request.data['text'])})
    elif request.method == 'GET':
        message = {'message': 'Hello, world! Welcome to the weird text format encoder!!!'}
        return Response(message)

@api_view(['POST', 'GET'])
def decoder(request):
    if request.method == 'POST':
        return Response({'decoded': decode(request.data['values'])})
        return Response(request.data)
    elif request.method == 'GET':
        message = {'message': 'Hello, world! Welcome to the weird text format decoder!!!'}
        return Response(message)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]