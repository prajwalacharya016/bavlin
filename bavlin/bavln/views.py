from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer


class ListItemView(APIView):
    """
    Provides a get method handler.
    """
    def get(self, request):
        queryset = Item.objects.all()
        serializer_class = ItemSerializer(queryset,many=True)
        return Response(serializer_class.data)

# Create your views here.
