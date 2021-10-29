from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.service.serializers import UserSerializer, GroupSerializer

from .models import Item

@api_view(['POST'])
def delete_item(request):
    Item.objects.get(id=request.data['id']).delete()
    return Response()

@api_view(['GET', 'POST'])
def item(request):

    if request.method == 'POST':
        Item.objects.create(
            item_name=request.data['itemName'],
            description=request.data['description'],
            amount=request.data['amount']
        )

    response_body = []

    # Add items from database to response body
    for curr_item in Item.objects.all():
        response_body.append({
            'itemName': curr_item.item_name,
            'description': curr_item.description,
            'amount': curr_item.amount
        })

    return Response(response_body)

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