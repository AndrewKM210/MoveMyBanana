from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response

from .models import Box, Product
from .serializers import SongsSerializer


class ListBoxes(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        queryset = Box.objects.all()
        # serializer_class = SongsSerializer
        return Response(queryset)


class CreateBox(generics.CreateAPIView):
    def post(self, request):
        box = request.POST.dict()
        Box.objects.create(id=box.id, type=box.type, posX=box.posX, posY=box.posY)
        Product.objects.create(name=box.product.name, quantity=box.product.quantity, box=box.id)
        return Response('OK')
