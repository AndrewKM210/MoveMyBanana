from django.http import HttpResponse
from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.utils import json

from .models import Box, Product, Instruction
from ImagineCode.serializers import BoxSerializer, InstructionSerializer


class ListBoxes(generics.ListAPIView):

    queryset = ''

    def get(self, request, *args):
        serialized_boxes = BoxSerializer(Box.objects.all(), many=True)
        return Response(serialized_boxes.data)


class ListInstructions(generics.ListAPIView):

    queryset = ''

    def get(self, request, *args):
        serialized_instructions = InstructionSerializer(Instruction.objects.all(), many=True)
        return Response(serialized_instructions.data)


class CreateBox(generics.CreateAPIView):

    def post(self, request, *args):
        box = json.loads(request.body.decode())
        box_foreign = Box.objects.create(id=box.get("id"), type=box.get("type"), posX=box.get("posX"), posY=box.get("posY"))
        products = box.get("products")
        for product in products:
            Product.objects.create(name=product.get("name"), quantity=product.get("quantity"), box=box_foreign)
        return Response('OK')


class CreateInstruction(generics.CreateAPIView):

    def post(self, request, *args):
        instruction = json.loads(request.body.decode())
        box = Box.objects.get(pk=instruction.get("box"))
        Instruction.objects.create(action=instruction.get("action"), name=instruction.get("name"), quantity=instruction.get("quantity"), box=box)
        return Response('OK')


class Resume(generics.ListAPIView):

    def get(self, request, *args):
        serialized_instructions = InstructionSerializer(Instruction.objects.first())
        return Response(serialized_instructions.data)


class TakeProduct(generics.UpdateAPIView):

    def post(self, request):
        id = ''





